from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class Disconnect(_message.Message):
    __slots__ = ("code", "reason")
    CODE_FIELD_NUMBER: _ClassVar[int]
    REASON_FIELD_NUMBER: _ClassVar[int]
    code: int
    reason: str
    def __init__(self, code: _Optional[int] = ..., reason: _Optional[str] = ...) -> None: ...

class Error(_message.Message):
    __slots__ = ("code", "message", "temporary")
    CODE_FIELD_NUMBER: _ClassVar[int]
    MESSAGE_FIELD_NUMBER: _ClassVar[int]
    TEMPORARY_FIELD_NUMBER: _ClassVar[int]
    code: int
    message: str
    temporary: bool
    def __init__(self, code: _Optional[int] = ..., message: _Optional[str] = ..., temporary: bool = ...) -> None: ...

class ConnectRequest(_message.Message):
    __slots__ = ("client", "transport", "protocol", "encoding", "data", "b64data", "name", "version", "channels")
    CLIENT_FIELD_NUMBER: _ClassVar[int]
    TRANSPORT_FIELD_NUMBER: _ClassVar[int]
    PROTOCOL_FIELD_NUMBER: _ClassVar[int]
    ENCODING_FIELD_NUMBER: _ClassVar[int]
    DATA_FIELD_NUMBER: _ClassVar[int]
    B64DATA_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    VERSION_FIELD_NUMBER: _ClassVar[int]
    CHANNELS_FIELD_NUMBER: _ClassVar[int]
    client: str
    transport: str
    protocol: str
    encoding: str
    data: bytes
    b64data: str
    name: str
    version: str
    channels: _containers.RepeatedScalarFieldContainer[str]
    def __init__(self, client: _Optional[str] = ..., transport: _Optional[str] = ..., protocol: _Optional[str] = ..., encoding: _Optional[str] = ..., data: _Optional[bytes] = ..., b64data: _Optional[str] = ..., name: _Optional[str] = ..., version: _Optional[str] = ..., channels: _Optional[_Iterable[str]] = ...) -> None: ...

class SubscribeOptions(_message.Message):
    __slots__ = ("expire_at", "info", "b64info", "data", "b64data", "override")
    EXPIRE_AT_FIELD_NUMBER: _ClassVar[int]
    INFO_FIELD_NUMBER: _ClassVar[int]
    B64INFO_FIELD_NUMBER: _ClassVar[int]
    DATA_FIELD_NUMBER: _ClassVar[int]
    B64DATA_FIELD_NUMBER: _ClassVar[int]
    OVERRIDE_FIELD_NUMBER: _ClassVar[int]
    expire_at: int
    info: bytes
    b64info: str
    data: bytes
    b64data: str
    override: SubscribeOptionOverride
    def __init__(self, expire_at: _Optional[int] = ..., info: _Optional[bytes] = ..., b64info: _Optional[str] = ..., data: _Optional[bytes] = ..., b64data: _Optional[str] = ..., override: _Optional[_Union[SubscribeOptionOverride, _Mapping]] = ...) -> None: ...

class ConnectResult(_message.Message):
    __slots__ = ("user", "expire_at", "info", "b64info", "data", "b64data", "channels", "subs", "meta", "caps")
    class SubsEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: SubscribeOptions
        def __init__(self, key: _Optional[str] = ..., value: _Optional[_Union[SubscribeOptions, _Mapping]] = ...) -> None: ...
    USER_FIELD_NUMBER: _ClassVar[int]
    EXPIRE_AT_FIELD_NUMBER: _ClassVar[int]
    INFO_FIELD_NUMBER: _ClassVar[int]
    B64INFO_FIELD_NUMBER: _ClassVar[int]
    DATA_FIELD_NUMBER: _ClassVar[int]
    B64DATA_FIELD_NUMBER: _ClassVar[int]
    CHANNELS_FIELD_NUMBER: _ClassVar[int]
    SUBS_FIELD_NUMBER: _ClassVar[int]
    META_FIELD_NUMBER: _ClassVar[int]
    CAPS_FIELD_NUMBER: _ClassVar[int]
    user: str
    expire_at: int
    info: bytes
    b64info: str
    data: bytes
    b64data: str
    channels: _containers.RepeatedScalarFieldContainer[str]
    subs: _containers.MessageMap[str, SubscribeOptions]
    meta: bytes
    caps: _containers.RepeatedCompositeFieldContainer[ChannelsCapability]
    def __init__(self, user: _Optional[str] = ..., expire_at: _Optional[int] = ..., info: _Optional[bytes] = ..., b64info: _Optional[str] = ..., data: _Optional[bytes] = ..., b64data: _Optional[str] = ..., channels: _Optional[_Iterable[str]] = ..., subs: _Optional[_Mapping[str, SubscribeOptions]] = ..., meta: _Optional[bytes] = ..., caps: _Optional[_Iterable[_Union[ChannelsCapability, _Mapping]]] = ...) -> None: ...

class ChannelsCapability(_message.Message):
    __slots__ = ("channels", "allow", "match")
    CHANNELS_FIELD_NUMBER: _ClassVar[int]
    ALLOW_FIELD_NUMBER: _ClassVar[int]
    MATCH_FIELD_NUMBER: _ClassVar[int]
    channels: _containers.RepeatedScalarFieldContainer[str]
    allow: _containers.RepeatedScalarFieldContainer[str]
    match: str
    def __init__(self, channels: _Optional[_Iterable[str]] = ..., allow: _Optional[_Iterable[str]] = ..., match: _Optional[str] = ...) -> None: ...

class ConnectResponse(_message.Message):
    __slots__ = ("result", "error", "disconnect")
    RESULT_FIELD_NUMBER: _ClassVar[int]
    ERROR_FIELD_NUMBER: _ClassVar[int]
    DISCONNECT_FIELD_NUMBER: _ClassVar[int]
    result: ConnectResult
    error: Error
    disconnect: Disconnect
    def __init__(self, result: _Optional[_Union[ConnectResult, _Mapping]] = ..., error: _Optional[_Union[Error, _Mapping]] = ..., disconnect: _Optional[_Union[Disconnect, _Mapping]] = ...) -> None: ...

class RefreshRequest(_message.Message):
    __slots__ = ("client", "transport", "protocol", "encoding", "user", "meta")
    CLIENT_FIELD_NUMBER: _ClassVar[int]
    TRANSPORT_FIELD_NUMBER: _ClassVar[int]
    PROTOCOL_FIELD_NUMBER: _ClassVar[int]
    ENCODING_FIELD_NUMBER: _ClassVar[int]
    USER_FIELD_NUMBER: _ClassVar[int]
    META_FIELD_NUMBER: _ClassVar[int]
    client: str
    transport: str
    protocol: str
    encoding: str
    user: str
    meta: bytes
    def __init__(self, client: _Optional[str] = ..., transport: _Optional[str] = ..., protocol: _Optional[str] = ..., encoding: _Optional[str] = ..., user: _Optional[str] = ..., meta: _Optional[bytes] = ...) -> None: ...

class RefreshResult(_message.Message):
    __slots__ = ("expired", "expire_at", "info", "b64info", "meta", "caps")
    EXPIRED_FIELD_NUMBER: _ClassVar[int]
    EXPIRE_AT_FIELD_NUMBER: _ClassVar[int]
    INFO_FIELD_NUMBER: _ClassVar[int]
    B64INFO_FIELD_NUMBER: _ClassVar[int]
    META_FIELD_NUMBER: _ClassVar[int]
    CAPS_FIELD_NUMBER: _ClassVar[int]
    expired: bool
    expire_at: int
    info: bytes
    b64info: str
    meta: bytes
    caps: _containers.RepeatedCompositeFieldContainer[ChannelsCapability]
    def __init__(self, expired: bool = ..., expire_at: _Optional[int] = ..., info: _Optional[bytes] = ..., b64info: _Optional[str] = ..., meta: _Optional[bytes] = ..., caps: _Optional[_Iterable[_Union[ChannelsCapability, _Mapping]]] = ...) -> None: ...

class RefreshResponse(_message.Message):
    __slots__ = ("result", "error", "disconnect")
    RESULT_FIELD_NUMBER: _ClassVar[int]
    ERROR_FIELD_NUMBER: _ClassVar[int]
    DISCONNECT_FIELD_NUMBER: _ClassVar[int]
    result: RefreshResult
    error: Error
    disconnect: Disconnect
    def __init__(self, result: _Optional[_Union[RefreshResult, _Mapping]] = ..., error: _Optional[_Union[Error, _Mapping]] = ..., disconnect: _Optional[_Union[Disconnect, _Mapping]] = ...) -> None: ...

class SubscribeRequest(_message.Message):
    __slots__ = ("client", "transport", "protocol", "encoding", "user", "channel", "token", "meta", "data", "b64data")
    CLIENT_FIELD_NUMBER: _ClassVar[int]
    TRANSPORT_FIELD_NUMBER: _ClassVar[int]
    PROTOCOL_FIELD_NUMBER: _ClassVar[int]
    ENCODING_FIELD_NUMBER: _ClassVar[int]
    USER_FIELD_NUMBER: _ClassVar[int]
    CHANNEL_FIELD_NUMBER: _ClassVar[int]
    TOKEN_FIELD_NUMBER: _ClassVar[int]
    META_FIELD_NUMBER: _ClassVar[int]
    DATA_FIELD_NUMBER: _ClassVar[int]
    B64DATA_FIELD_NUMBER: _ClassVar[int]
    client: str
    transport: str
    protocol: str
    encoding: str
    user: str
    channel: str
    token: str
    meta: bytes
    data: bytes
    b64data: str
    def __init__(self, client: _Optional[str] = ..., transport: _Optional[str] = ..., protocol: _Optional[str] = ..., encoding: _Optional[str] = ..., user: _Optional[str] = ..., channel: _Optional[str] = ..., token: _Optional[str] = ..., meta: _Optional[bytes] = ..., data: _Optional[bytes] = ..., b64data: _Optional[str] = ...) -> None: ...

class BoolValue(_message.Message):
    __slots__ = ("value",)
    VALUE_FIELD_NUMBER: _ClassVar[int]
    value: bool
    def __init__(self, value: bool = ...) -> None: ...

class Int32Value(_message.Message):
    __slots__ = ("value",)
    VALUE_FIELD_NUMBER: _ClassVar[int]
    value: int
    def __init__(self, value: _Optional[int] = ...) -> None: ...

class SubscribeOptionOverride(_message.Message):
    __slots__ = ("presence", "join_leave", "force_recovery", "force_positioning", "force_push_join_leave")
    PRESENCE_FIELD_NUMBER: _ClassVar[int]
    JOIN_LEAVE_FIELD_NUMBER: _ClassVar[int]
    FORCE_RECOVERY_FIELD_NUMBER: _ClassVar[int]
    FORCE_POSITIONING_FIELD_NUMBER: _ClassVar[int]
    FORCE_PUSH_JOIN_LEAVE_FIELD_NUMBER: _ClassVar[int]
    presence: BoolValue
    join_leave: BoolValue
    force_recovery: BoolValue
    force_positioning: BoolValue
    force_push_join_leave: BoolValue
    def __init__(self, presence: _Optional[_Union[BoolValue, _Mapping]] = ..., join_leave: _Optional[_Union[BoolValue, _Mapping]] = ..., force_recovery: _Optional[_Union[BoolValue, _Mapping]] = ..., force_positioning: _Optional[_Union[BoolValue, _Mapping]] = ..., force_push_join_leave: _Optional[_Union[BoolValue, _Mapping]] = ...) -> None: ...

class SubscribeResult(_message.Message):
    __slots__ = ("expire_at", "info", "b64info", "data", "b64data", "override", "allow")
    EXPIRE_AT_FIELD_NUMBER: _ClassVar[int]
    INFO_FIELD_NUMBER: _ClassVar[int]
    B64INFO_FIELD_NUMBER: _ClassVar[int]
    DATA_FIELD_NUMBER: _ClassVar[int]
    B64DATA_FIELD_NUMBER: _ClassVar[int]
    OVERRIDE_FIELD_NUMBER: _ClassVar[int]
    ALLOW_FIELD_NUMBER: _ClassVar[int]
    expire_at: int
    info: bytes
    b64info: str
    data: bytes
    b64data: str
    override: SubscribeOptionOverride
    allow: _containers.RepeatedScalarFieldContainer[str]
    def __init__(self, expire_at: _Optional[int] = ..., info: _Optional[bytes] = ..., b64info: _Optional[str] = ..., data: _Optional[bytes] = ..., b64data: _Optional[str] = ..., override: _Optional[_Union[SubscribeOptionOverride, _Mapping]] = ..., allow: _Optional[_Iterable[str]] = ...) -> None: ...

class SubscribeResponse(_message.Message):
    __slots__ = ("result", "error", "disconnect")
    RESULT_FIELD_NUMBER: _ClassVar[int]
    ERROR_FIELD_NUMBER: _ClassVar[int]
    DISCONNECT_FIELD_NUMBER: _ClassVar[int]
    result: SubscribeResult
    error: Error
    disconnect: Disconnect
    def __init__(self, result: _Optional[_Union[SubscribeResult, _Mapping]] = ..., error: _Optional[_Union[Error, _Mapping]] = ..., disconnect: _Optional[_Union[Disconnect, _Mapping]] = ...) -> None: ...

class PublishRequest(_message.Message):
    __slots__ = ("client", "transport", "protocol", "encoding", "user", "channel", "data", "b64data", "meta")
    CLIENT_FIELD_NUMBER: _ClassVar[int]
    TRANSPORT_FIELD_NUMBER: _ClassVar[int]
    PROTOCOL_FIELD_NUMBER: _ClassVar[int]
    ENCODING_FIELD_NUMBER: _ClassVar[int]
    USER_FIELD_NUMBER: _ClassVar[int]
    CHANNEL_FIELD_NUMBER: _ClassVar[int]
    DATA_FIELD_NUMBER: _ClassVar[int]
    B64DATA_FIELD_NUMBER: _ClassVar[int]
    META_FIELD_NUMBER: _ClassVar[int]
    client: str
    transport: str
    protocol: str
    encoding: str
    user: str
    channel: str
    data: bytes
    b64data: str
    meta: bytes
    def __init__(self, client: _Optional[str] = ..., transport: _Optional[str] = ..., protocol: _Optional[str] = ..., encoding: _Optional[str] = ..., user: _Optional[str] = ..., channel: _Optional[str] = ..., data: _Optional[bytes] = ..., b64data: _Optional[str] = ..., meta: _Optional[bytes] = ...) -> None: ...

class PublishResult(_message.Message):
    __slots__ = ("data", "b64data", "skip_history")
    DATA_FIELD_NUMBER: _ClassVar[int]
    B64DATA_FIELD_NUMBER: _ClassVar[int]
    SKIP_HISTORY_FIELD_NUMBER: _ClassVar[int]
    data: bytes
    b64data: str
    skip_history: bool
    def __init__(self, data: _Optional[bytes] = ..., b64data: _Optional[str] = ..., skip_history: bool = ...) -> None: ...

class PublishResponse(_message.Message):
    __slots__ = ("result", "error", "disconnect")
    RESULT_FIELD_NUMBER: _ClassVar[int]
    ERROR_FIELD_NUMBER: _ClassVar[int]
    DISCONNECT_FIELD_NUMBER: _ClassVar[int]
    result: PublishResult
    error: Error
    disconnect: Disconnect
    def __init__(self, result: _Optional[_Union[PublishResult, _Mapping]] = ..., error: _Optional[_Union[Error, _Mapping]] = ..., disconnect: _Optional[_Union[Disconnect, _Mapping]] = ...) -> None: ...

class RPCRequest(_message.Message):
    __slots__ = ("client", "transport", "protocol", "encoding", "user", "method", "data", "b64data", "meta")
    CLIENT_FIELD_NUMBER: _ClassVar[int]
    TRANSPORT_FIELD_NUMBER: _ClassVar[int]
    PROTOCOL_FIELD_NUMBER: _ClassVar[int]
    ENCODING_FIELD_NUMBER: _ClassVar[int]
    USER_FIELD_NUMBER: _ClassVar[int]
    METHOD_FIELD_NUMBER: _ClassVar[int]
    DATA_FIELD_NUMBER: _ClassVar[int]
    B64DATA_FIELD_NUMBER: _ClassVar[int]
    META_FIELD_NUMBER: _ClassVar[int]
    client: str
    transport: str
    protocol: str
    encoding: str
    user: str
    method: str
    data: bytes
    b64data: str
    meta: bytes
    def __init__(self, client: _Optional[str] = ..., transport: _Optional[str] = ..., protocol: _Optional[str] = ..., encoding: _Optional[str] = ..., user: _Optional[str] = ..., method: _Optional[str] = ..., data: _Optional[bytes] = ..., b64data: _Optional[str] = ..., meta: _Optional[bytes] = ...) -> None: ...

class RPCResult(_message.Message):
    __slots__ = ("data", "b64data")
    DATA_FIELD_NUMBER: _ClassVar[int]
    B64DATA_FIELD_NUMBER: _ClassVar[int]
    data: bytes
    b64data: str
    def __init__(self, data: _Optional[bytes] = ..., b64data: _Optional[str] = ...) -> None: ...

class RPCResponse(_message.Message):
    __slots__ = ("result", "error", "disconnect")
    RESULT_FIELD_NUMBER: _ClassVar[int]
    ERROR_FIELD_NUMBER: _ClassVar[int]
    DISCONNECT_FIELD_NUMBER: _ClassVar[int]
    result: RPCResult
    error: Error
    disconnect: Disconnect
    def __init__(self, result: _Optional[_Union[RPCResult, _Mapping]] = ..., error: _Optional[_Union[Error, _Mapping]] = ..., disconnect: _Optional[_Union[Disconnect, _Mapping]] = ...) -> None: ...

class SubRefreshRequest(_message.Message):
    __slots__ = ("client", "transport", "protocol", "encoding", "user", "channel", "meta")
    CLIENT_FIELD_NUMBER: _ClassVar[int]
    TRANSPORT_FIELD_NUMBER: _ClassVar[int]
    PROTOCOL_FIELD_NUMBER: _ClassVar[int]
    ENCODING_FIELD_NUMBER: _ClassVar[int]
    USER_FIELD_NUMBER: _ClassVar[int]
    CHANNEL_FIELD_NUMBER: _ClassVar[int]
    META_FIELD_NUMBER: _ClassVar[int]
    client: str
    transport: str
    protocol: str
    encoding: str
    user: str
    channel: str
    meta: bytes
    def __init__(self, client: _Optional[str] = ..., transport: _Optional[str] = ..., protocol: _Optional[str] = ..., encoding: _Optional[str] = ..., user: _Optional[str] = ..., channel: _Optional[str] = ..., meta: _Optional[bytes] = ...) -> None: ...

class SubRefreshResult(_message.Message):
    __slots__ = ("expired", "expire_at", "info", "b64info")
    EXPIRED_FIELD_NUMBER: _ClassVar[int]
    EXPIRE_AT_FIELD_NUMBER: _ClassVar[int]
    INFO_FIELD_NUMBER: _ClassVar[int]
    B64INFO_FIELD_NUMBER: _ClassVar[int]
    expired: bool
    expire_at: int
    info: bytes
    b64info: str
    def __init__(self, expired: bool = ..., expire_at: _Optional[int] = ..., info: _Optional[bytes] = ..., b64info: _Optional[str] = ...) -> None: ...

class SubRefreshResponse(_message.Message):
    __slots__ = ("result", "error", "disconnect")
    RESULT_FIELD_NUMBER: _ClassVar[int]
    ERROR_FIELD_NUMBER: _ClassVar[int]
    DISCONNECT_FIELD_NUMBER: _ClassVar[int]
    result: SubRefreshResult
    error: Error
    disconnect: Disconnect
    def __init__(self, result: _Optional[_Union[SubRefreshResult, _Mapping]] = ..., error: _Optional[_Union[Error, _Mapping]] = ..., disconnect: _Optional[_Union[Disconnect, _Mapping]] = ...) -> None: ...

class Publication(_message.Message):
    __slots__ = ("data", "tags")
    class TagsEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: str
        def __init__(self, key: _Optional[str] = ..., value: _Optional[str] = ...) -> None: ...
    DATA_FIELD_NUMBER: _ClassVar[int]
    TAGS_FIELD_NUMBER: _ClassVar[int]
    data: bytes
    tags: _containers.ScalarMap[str, str]
    def __init__(self, data: _Optional[bytes] = ..., tags: _Optional[_Mapping[str, str]] = ...) -> None: ...

class StreamSubscribeRequest(_message.Message):
    __slots__ = ("subscribe_request", "publication")
    SUBSCRIBE_REQUEST_FIELD_NUMBER: _ClassVar[int]
    PUBLICATION_FIELD_NUMBER: _ClassVar[int]
    subscribe_request: SubscribeRequest
    publication: Publication
    def __init__(self, subscribe_request: _Optional[_Union[SubscribeRequest, _Mapping]] = ..., publication: _Optional[_Union[Publication, _Mapping]] = ...) -> None: ...

class StreamSubscribeResponse(_message.Message):
    __slots__ = ("subscribe_response", "publication")
    SUBSCRIBE_RESPONSE_FIELD_NUMBER: _ClassVar[int]
    PUBLICATION_FIELD_NUMBER: _ClassVar[int]
    subscribe_response: SubscribeResponse
    publication: Publication
    def __init__(self, subscribe_response: _Optional[_Union[SubscribeResponse, _Mapping]] = ..., publication: _Optional[_Union[Publication, _Mapping]] = ...) -> None: ...

class NotifyCacheEmptyRequest(_message.Message):
    __slots__ = ("channel",)
    CHANNEL_FIELD_NUMBER: _ClassVar[int]
    channel: str
    def __init__(self, channel: _Optional[str] = ...) -> None: ...

class NotifyCacheEmptyResponse(_message.Message):
    __slots__ = ("result",)
    RESULT_FIELD_NUMBER: _ClassVar[int]
    result: NotifyCacheEmptyResult
    def __init__(self, result: _Optional[_Union[NotifyCacheEmptyResult, _Mapping]] = ...) -> None: ...

class NotifyCacheEmptyResult(_message.Message):
    __slots__ = ("populated",)
    POPULATED_FIELD_NUMBER: _ClassVar[int]
    populated: bool
    def __init__(self, populated: bool = ...) -> None: ...

class NotifyChannelStateRequest(_message.Message):
    __slots__ = ("events",)
    EVENTS_FIELD_NUMBER: _ClassVar[int]
    events: _containers.RepeatedCompositeFieldContainer[ChannelEvent]
    def __init__(self, events: _Optional[_Iterable[_Union[ChannelEvent, _Mapping]]] = ...) -> None: ...

class ChannelEvent(_message.Message):
    __slots__ = ("time_ms", "channel", "type")
    TIME_MS_FIELD_NUMBER: _ClassVar[int]
    CHANNEL_FIELD_NUMBER: _ClassVar[int]
    TYPE_FIELD_NUMBER: _ClassVar[int]
    time_ms: int
    channel: str
    type: str
    def __init__(self, time_ms: _Optional[int] = ..., channel: _Optional[str] = ..., type: _Optional[str] = ...) -> None: ...

class NotifyChannelStateResponse(_message.Message):
    __slots__ = ("result", "error")
    RESULT_FIELD_NUMBER: _ClassVar[int]
    ERROR_FIELD_NUMBER: _ClassVar[int]
    result: NotifyChannelStateResult
    error: Error
    def __init__(self, result: _Optional[_Union[NotifyChannelStateResult, _Mapping]] = ..., error: _Optional[_Union[Error, _Mapping]] = ...) -> None: ...

class NotifyChannelStateResult(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...
