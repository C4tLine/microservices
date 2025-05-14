import json
import httpx
import datetime

import grpc
import jwt

from src.api.grpc.protobufs import proxy_pb2_grpc, proxy_pb2
from src.api.sqlc import ws_requests
from src.storage.postgres import engine
from config import settings

key_begin = '-----BEGIN PUBLIC KEY-----\n'
key_end = '\n-----END PUBLIC KEY-----'
client_key = ''
backend_key = {
    'token': '',
    'expire_at': datetime.datetime.now(),
}

class ProxyService(proxy_pb2_grpc.CentrifugoProxyServicer):
    @staticmethod
    async def serve() -> None:
        server = grpc.aio.server()
        proxy_pb2_grpc.add_CentrifugoProxyServicer_to_server(ProxyService(), server)
        server.add_insecure_port('[::]:1337')
        await server.start()
        await server.wait_for_termination()

    async def Connect(
        self,
        request: proxy_pb2.ConnectRequest,
        context: grpc.aio.ServicerContext,
    ) -> proxy_pb2.ConnectResponse:
        data = json.loads(request.data.decode())
        global client_key
        if not client_key:
            async with httpx.AsyncClient() as client:
                config_data = (await client.get('http://localhost:7070/realms/newrealm')).json()
            client_key = config_data['public_key']
            if not client_key.startswith(key_begin):
                client_key = f'{key_begin}{client_key}'
            if not client_key.endswith(key_end):
                client_key = f'{client_key}{key_end}'
        token_data =jwt.decode(data['token'], client_key, algorithms=['RS256'], audience='account', verify=True)
        user_id = token_data['sub']
        async with engine.connect() as connection:
            querier = ws_requests.AsyncQuerier(connection)
            user = await querier.get_user_by_id(id=user_id)
            if not user:
                if backend_key['expire_at'] < datetime.datetime.now():
                    async with httpx.AsyncClient() as client:
                        backend_token = await client.post(
                            'http://localhost:7070/realms/newrealm/protocol/openid-connect/token',
                            headers={
                                'Content-Type': 'application/x-www-form-urlencoded',
                            },
                            data={
                                'client_id': 'backend',
                                'grant_type': 'client_credentials',
                                'client_secret': settings.KC_BACKEND_SECRET.get_secret_value(),
                            },
                        )
                        backend_token = backend_token.json()
                    backend_key['token'] = backend_token['access_token']
                    backend_key['expire_at'] = datetime.datetime.now() + datetime.timedelta(seconds=backend_token['expires_in'])
                async with httpx.AsyncClient() as client:
                    kc_user_data = (await client.get(
                        f'http://localhost:8080/admin/realms/newrealm/users/{user_id}',
                        headers={
                            'Authorization': f'Bearer {backend_key["token"]}'
                        }
                    )).json()
                user_data = {
                    'id': kc_user_data['id'],
                    'username': kc_user_data['username'],
                    'given_name': kc_user_data['firstName'],
                    'family_name': kc_user_data['lastName'],
                    'email': kc_user_data['email'],
                }
                await querier.create_user(
                    id=user_data['id'],
                    username=user_data['username'],
                    given_name=user_data['given_name'],
                    family_name=user_data['family_name'],
                    enabled=True,
                )
            await connection.commit()
        return proxy_pb2.ConnectResponse(
            result=proxy_pb2.ConnectResult(
                user=user_id,
            ),
        )

    async def Subscribe(
        self,
        request: proxy_pb2.SubscribeRequest,
        context: grpc.aio.ServicerContext,
    ) -> proxy_pb2.SubscribeResponse:
        async with engine.connect() as connection:
            querier = ws_requests.AsyncQuerier(connection)
            await querier.subscribe_user_to_channel(
                user_id=request.user,
                channel=request.channel,
                can_publish=True,
            )
            await connection.commit()
        return proxy_pb2.SubscribeResponse(
            result=proxy_pb2.SubscribeResult(
                info=json.dumps({"can_publish": "aaaa"}).encode()
            )
        )

    async def Publish(
        self,
        request: proxy_pb2.PublishRequest,
        context: grpc.aio.ServicerContext,
    ) -> proxy_pb2.PublishResponse:
        async with engine.connect() as connection:
            querier = ws_requests.AsyncQuerier(connection)
            can_publish = await querier.user_can_publish(
                user_id=request.user,
                channel=request.channel,
            )
        if can_publish:
            return proxy_pb2.PublishResponse()
        return proxy_pb2.PublishResponse(
            error=proxy_pb2.Error(code=103),
        )

    async def RPC(
        self,
        request: proxy_pb2.RPCRequest,
        context: grpc.aio.ServicerContext,
    ) -> proxy_pb2.RPCResponse:
        if request.method == 'get_user_channels':
            async with engine.connect() as connection:
                querier = ws_requests.AsyncQuerier(connection)
                channels = [channel.channel async for channel in querier.chan_list_by_user_id(user_id=request.user)]
            return proxy_pb2.RPCResponse(
                result=proxy_pb2.RPCResult(
                    data=f'{{ "channels": {json.dumps(channels)} }}'.encode(),
                ),
            )
        return super().RPC(request, context)
