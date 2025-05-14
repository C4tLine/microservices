import asyncio
from contextlib import asynccontextmanager
from typing import AsyncGenerator

import uvicorn
from fastapi import FastAPI

from config import logger
from src.api.grpc.services import ProxyService

logger = logger(__name__)


@asynccontextmanager
async def lifespan(app: FastAPI) -> AsyncGenerator[None, None]:
    grpc_task = asyncio.create_task(ProxyService.serve())
    yield
    grpc_task.cancel()


def create_app() -> FastAPI:
    return FastAPI(docs_url='/swagger', lifespan=lifespan)


if __name__ == '__main__':
    uvicorn.run(
        'src.__main__:create_app',
        factory=True,
        host='127.0.0.1',
        port=8001,
        workers=1,
        access_log=False,
    )
