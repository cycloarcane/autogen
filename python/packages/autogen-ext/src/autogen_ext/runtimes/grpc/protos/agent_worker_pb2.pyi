"""
@generated by mypy-protobuf.  Do not edit manually!
isort:skip_file
"""

import builtins
import collections.abc
import typing

import cloudevent_pb2
import google.protobuf.any_pb2
import google.protobuf.descriptor
import google.protobuf.internal.containers
import google.protobuf.message

DESCRIPTOR: google.protobuf.descriptor.FileDescriptor

@typing.final
class TopicId(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    TYPE_FIELD_NUMBER: builtins.int
    SOURCE_FIELD_NUMBER: builtins.int
    type: builtins.str
    source: builtins.str
    def __init__(
        self,
        *,
        type: builtins.str = ...,
        source: builtins.str = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing.Literal["source", b"source", "type", b"type"]) -> None: ...

global___TopicId = TopicId

@typing.final
class AgentId(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    TYPE_FIELD_NUMBER: builtins.int
    KEY_FIELD_NUMBER: builtins.int
    type: builtins.str
    key: builtins.str
    def __init__(
        self,
        *,
        type: builtins.str = ...,
        key: builtins.str = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing.Literal["key", b"key", "type", b"type"]) -> None: ...

global___AgentId = AgentId

@typing.final
class Payload(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    DATA_TYPE_FIELD_NUMBER: builtins.int
    DATA_CONTENT_TYPE_FIELD_NUMBER: builtins.int
    DATA_FIELD_NUMBER: builtins.int
    data_type: builtins.str
    data_content_type: builtins.str
    data: builtins.bytes
    def __init__(
        self,
        *,
        data_type: builtins.str = ...,
        data_content_type: builtins.str = ...,
        data: builtins.bytes = ...,
    ) -> None: ...
    def ClearField(
        self,
        field_name: typing.Literal[
            "data", b"data", "data_content_type", b"data_content_type", "data_type", b"data_type"
        ],
    ) -> None: ...

global___Payload = Payload

@typing.final
class RpcRequest(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    @typing.final
    class MetadataEntry(google.protobuf.message.Message):
        DESCRIPTOR: google.protobuf.descriptor.Descriptor

        KEY_FIELD_NUMBER: builtins.int
        VALUE_FIELD_NUMBER: builtins.int
        key: builtins.str
        value: builtins.str
        def __init__(
            self,
            *,
            key: builtins.str = ...,
            value: builtins.str = ...,
        ) -> None: ...
        def ClearField(self, field_name: typing.Literal["key", b"key", "value", b"value"]) -> None: ...

    REQUEST_ID_FIELD_NUMBER: builtins.int
    SOURCE_FIELD_NUMBER: builtins.int
    TARGET_FIELD_NUMBER: builtins.int
    METHOD_FIELD_NUMBER: builtins.int
    PAYLOAD_FIELD_NUMBER: builtins.int
    METADATA_FIELD_NUMBER: builtins.int
    request_id: builtins.str
    method: builtins.str
    @property
    def source(self) -> global___AgentId: ...
    @property
    def target(self) -> global___AgentId: ...
    @property
    def payload(self) -> global___Payload: ...
    @property
    def metadata(self) -> google.protobuf.internal.containers.ScalarMap[builtins.str, builtins.str]: ...
    def __init__(
        self,
        *,
        request_id: builtins.str = ...,
        source: global___AgentId | None = ...,
        target: global___AgentId | None = ...,
        method: builtins.str = ...,
        payload: global___Payload | None = ...,
        metadata: collections.abc.Mapping[builtins.str, builtins.str] | None = ...,
    ) -> None: ...
    def HasField(
        self,
        field_name: typing.Literal[
            "_source", b"_source", "payload", b"payload", "source", b"source", "target", b"target"
        ],
    ) -> builtins.bool: ...
    def ClearField(
        self,
        field_name: typing.Literal[
            "_source",
            b"_source",
            "metadata",
            b"metadata",
            "method",
            b"method",
            "payload",
            b"payload",
            "request_id",
            b"request_id",
            "source",
            b"source",
            "target",
            b"target",
        ],
    ) -> None: ...
    def WhichOneof(self, oneof_group: typing.Literal["_source", b"_source"]) -> typing.Literal["source"] | None: ...

global___RpcRequest = RpcRequest

@typing.final
class RpcResponse(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    @typing.final
    class MetadataEntry(google.protobuf.message.Message):
        DESCRIPTOR: google.protobuf.descriptor.Descriptor

        KEY_FIELD_NUMBER: builtins.int
        VALUE_FIELD_NUMBER: builtins.int
        key: builtins.str
        value: builtins.str
        def __init__(
            self,
            *,
            key: builtins.str = ...,
            value: builtins.str = ...,
        ) -> None: ...
        def ClearField(self, field_name: typing.Literal["key", b"key", "value", b"value"]) -> None: ...

    REQUEST_ID_FIELD_NUMBER: builtins.int
    PAYLOAD_FIELD_NUMBER: builtins.int
    ERROR_FIELD_NUMBER: builtins.int
    METADATA_FIELD_NUMBER: builtins.int
    request_id: builtins.str
    error: builtins.str
    @property
    def payload(self) -> global___Payload: ...
    @property
    def metadata(self) -> google.protobuf.internal.containers.ScalarMap[builtins.str, builtins.str]: ...
    def __init__(
        self,
        *,
        request_id: builtins.str = ...,
        payload: global___Payload | None = ...,
        error: builtins.str = ...,
        metadata: collections.abc.Mapping[builtins.str, builtins.str] | None = ...,
    ) -> None: ...
    def HasField(self, field_name: typing.Literal["payload", b"payload"]) -> builtins.bool: ...
    def ClearField(
        self,
        field_name: typing.Literal[
            "error", b"error", "metadata", b"metadata", "payload", b"payload", "request_id", b"request_id"
        ],
    ) -> None: ...

global___RpcResponse = RpcResponse

@typing.final
class Event(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    @typing.final
    class MetadataEntry(google.protobuf.message.Message):
        DESCRIPTOR: google.protobuf.descriptor.Descriptor

        KEY_FIELD_NUMBER: builtins.int
        VALUE_FIELD_NUMBER: builtins.int
        key: builtins.str
        value: builtins.str
        def __init__(
            self,
            *,
            key: builtins.str = ...,
            value: builtins.str = ...,
        ) -> None: ...
        def ClearField(self, field_name: typing.Literal["key", b"key", "value", b"value"]) -> None: ...

    TOPIC_TYPE_FIELD_NUMBER: builtins.int
    TOPIC_SOURCE_FIELD_NUMBER: builtins.int
    SOURCE_FIELD_NUMBER: builtins.int
    PAYLOAD_FIELD_NUMBER: builtins.int
    METADATA_FIELD_NUMBER: builtins.int
    topic_type: builtins.str
    topic_source: builtins.str
    @property
    def source(self) -> global___AgentId: ...
    @property
    def payload(self) -> global___Payload: ...
    @property
    def metadata(self) -> google.protobuf.internal.containers.ScalarMap[builtins.str, builtins.str]: ...
    def __init__(
        self,
        *,
        topic_type: builtins.str = ...,
        topic_source: builtins.str = ...,
        source: global___AgentId | None = ...,
        payload: global___Payload | None = ...,
        metadata: collections.abc.Mapping[builtins.str, builtins.str] | None = ...,
    ) -> None: ...
    def HasField(
        self, field_name: typing.Literal["_source", b"_source", "payload", b"payload", "source", b"source"]
    ) -> builtins.bool: ...
    def ClearField(
        self,
        field_name: typing.Literal[
            "_source",
            b"_source",
            "metadata",
            b"metadata",
            "payload",
            b"payload",
            "source",
            b"source",
            "topic_source",
            b"topic_source",
            "topic_type",
            b"topic_type",
        ],
    ) -> None: ...
    def WhichOneof(self, oneof_group: typing.Literal["_source", b"_source"]) -> typing.Literal["source"] | None: ...

global___Event = Event

@typing.final
class RegisterAgentTypeRequest(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    REQUEST_ID_FIELD_NUMBER: builtins.int
    TYPE_FIELD_NUMBER: builtins.int
    request_id: builtins.str
    type: builtins.str
    def __init__(
        self,
        *,
        request_id: builtins.str = ...,
        type: builtins.str = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing.Literal["request_id", b"request_id", "type", b"type"]) -> None: ...

global___RegisterAgentTypeRequest = RegisterAgentTypeRequest

@typing.final
class RegisterAgentTypeResponse(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    REQUEST_ID_FIELD_NUMBER: builtins.int
    SUCCESS_FIELD_NUMBER: builtins.int
    ERROR_FIELD_NUMBER: builtins.int
    request_id: builtins.str
    success: builtins.bool
    error: builtins.str
    def __init__(
        self,
        *,
        request_id: builtins.str = ...,
        success: builtins.bool = ...,
        error: builtins.str | None = ...,
    ) -> None: ...
    def HasField(self, field_name: typing.Literal["_error", b"_error", "error", b"error"]) -> builtins.bool: ...
    def ClearField(
        self,
        field_name: typing.Literal[
            "_error", b"_error", "error", b"error", "request_id", b"request_id", "success", b"success"
        ],
    ) -> None: ...
    def WhichOneof(self, oneof_group: typing.Literal["_error", b"_error"]) -> typing.Literal["error"] | None: ...

global___RegisterAgentTypeResponse = RegisterAgentTypeResponse

@typing.final
class TypeSubscription(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    TOPIC_TYPE_FIELD_NUMBER: builtins.int
    AGENT_TYPE_FIELD_NUMBER: builtins.int
    topic_type: builtins.str
    agent_type: builtins.str
    def __init__(
        self,
        *,
        topic_type: builtins.str = ...,
        agent_type: builtins.str = ...,
    ) -> None: ...
    def ClearField(
        self, field_name: typing.Literal["agent_type", b"agent_type", "topic_type", b"topic_type"]
    ) -> None: ...

global___TypeSubscription = TypeSubscription

@typing.final
class TypePrefixSubscription(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    TOPIC_TYPE_PREFIX_FIELD_NUMBER: builtins.int
    AGENT_TYPE_FIELD_NUMBER: builtins.int
    topic_type_prefix: builtins.str
    agent_type: builtins.str
    def __init__(
        self,
        *,
        topic_type_prefix: builtins.str = ...,
        agent_type: builtins.str = ...,
    ) -> None: ...
    def ClearField(
        self, field_name: typing.Literal["agent_type", b"agent_type", "topic_type_prefix", b"topic_type_prefix"]
    ) -> None: ...

global___TypePrefixSubscription = TypePrefixSubscription

@typing.final
class Subscription(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    TYPESUBSCRIPTION_FIELD_NUMBER: builtins.int
    TYPEPREFIXSUBSCRIPTION_FIELD_NUMBER: builtins.int
    @property
    def typeSubscription(self) -> global___TypeSubscription: ...
    @property
    def typePrefixSubscription(self) -> global___TypePrefixSubscription: ...
    def __init__(
        self,
        *,
        typeSubscription: global___TypeSubscription | None = ...,
        typePrefixSubscription: global___TypePrefixSubscription | None = ...,
    ) -> None: ...
    def HasField(
        self,
        field_name: typing.Literal[
            "subscription",
            b"subscription",
            "typePrefixSubscription",
            b"typePrefixSubscription",
            "typeSubscription",
            b"typeSubscription",
        ],
    ) -> builtins.bool: ...
    def ClearField(
        self,
        field_name: typing.Literal[
            "subscription",
            b"subscription",
            "typePrefixSubscription",
            b"typePrefixSubscription",
            "typeSubscription",
            b"typeSubscription",
        ],
    ) -> None: ...
    def WhichOneof(
        self, oneof_group: typing.Literal["subscription", b"subscription"]
    ) -> typing.Literal["typeSubscription", "typePrefixSubscription"] | None: ...

global___Subscription = Subscription

@typing.final
class AddSubscriptionRequest(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    REQUEST_ID_FIELD_NUMBER: builtins.int
    SUBSCRIPTION_FIELD_NUMBER: builtins.int
    request_id: builtins.str
    @property
    def subscription(self) -> global___Subscription: ...
    def __init__(
        self,
        *,
        request_id: builtins.str = ...,
        subscription: global___Subscription | None = ...,
    ) -> None: ...
    def HasField(self, field_name: typing.Literal["subscription", b"subscription"]) -> builtins.bool: ...
    def ClearField(
        self, field_name: typing.Literal["request_id", b"request_id", "subscription", b"subscription"]
    ) -> None: ...

global___AddSubscriptionRequest = AddSubscriptionRequest

@typing.final
class AddSubscriptionResponse(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    REQUEST_ID_FIELD_NUMBER: builtins.int
    SUCCESS_FIELD_NUMBER: builtins.int
    ERROR_FIELD_NUMBER: builtins.int
    request_id: builtins.str
    success: builtins.bool
    error: builtins.str
    def __init__(
        self,
        *,
        request_id: builtins.str = ...,
        success: builtins.bool = ...,
        error: builtins.str | None = ...,
    ) -> None: ...
    def HasField(self, field_name: typing.Literal["_error", b"_error", "error", b"error"]) -> builtins.bool: ...
    def ClearField(
        self,
        field_name: typing.Literal[
            "_error", b"_error", "error", b"error", "request_id", b"request_id", "success", b"success"
        ],
    ) -> None: ...
    def WhichOneof(self, oneof_group: typing.Literal["_error", b"_error"]) -> typing.Literal["error"] | None: ...

global___AddSubscriptionResponse = AddSubscriptionResponse

@typing.final
class AgentState(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    AGENT_ID_FIELD_NUMBER: builtins.int
    ETAG_FIELD_NUMBER: builtins.int
    BINARY_DATA_FIELD_NUMBER: builtins.int
    TEXT_DATA_FIELD_NUMBER: builtins.int
    PROTO_DATA_FIELD_NUMBER: builtins.int
    eTag: builtins.str
    binary_data: builtins.bytes
    text_data: builtins.str
    @property
    def agent_id(self) -> global___AgentId: ...
    @property
    def proto_data(self) -> google.protobuf.any_pb2.Any: ...
    def __init__(
        self,
        *,
        agent_id: global___AgentId | None = ...,
        eTag: builtins.str = ...,
        binary_data: builtins.bytes = ...,
        text_data: builtins.str = ...,
        proto_data: google.protobuf.any_pb2.Any | None = ...,
    ) -> None: ...
    def HasField(
        self,
        field_name: typing.Literal[
            "agent_id",
            b"agent_id",
            "binary_data",
            b"binary_data",
            "data",
            b"data",
            "proto_data",
            b"proto_data",
            "text_data",
            b"text_data",
        ],
    ) -> builtins.bool: ...
    def ClearField(
        self,
        field_name: typing.Literal[
            "agent_id",
            b"agent_id",
            "binary_data",
            b"binary_data",
            "data",
            b"data",
            "eTag",
            b"eTag",
            "proto_data",
            b"proto_data",
            "text_data",
            b"text_data",
        ],
    ) -> None: ...
    def WhichOneof(
        self, oneof_group: typing.Literal["data", b"data"]
    ) -> typing.Literal["binary_data", "text_data", "proto_data"] | None: ...

global___AgentState = AgentState

@typing.final
class GetStateResponse(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    AGENT_STATE_FIELD_NUMBER: builtins.int
    SUCCESS_FIELD_NUMBER: builtins.int
    ERROR_FIELD_NUMBER: builtins.int
    success: builtins.bool
    error: builtins.str
    @property
    def agent_state(self) -> global___AgentState: ...
    def __init__(
        self,
        *,
        agent_state: global___AgentState | None = ...,
        success: builtins.bool = ...,
        error: builtins.str | None = ...,
    ) -> None: ...
    def HasField(
        self, field_name: typing.Literal["_error", b"_error", "agent_state", b"agent_state", "error", b"error"]
    ) -> builtins.bool: ...
    def ClearField(
        self,
        field_name: typing.Literal[
            "_error", b"_error", "agent_state", b"agent_state", "error", b"error", "success", b"success"
        ],
    ) -> None: ...
    def WhichOneof(self, oneof_group: typing.Literal["_error", b"_error"]) -> typing.Literal["error"] | None: ...

global___GetStateResponse = GetStateResponse

@typing.final
class SaveStateResponse(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    SUCCESS_FIELD_NUMBER: builtins.int
    ERROR_FIELD_NUMBER: builtins.int
    success: builtins.bool
    error: builtins.str
    def __init__(
        self,
        *,
        success: builtins.bool = ...,
        error: builtins.str | None = ...,
    ) -> None: ...
    def HasField(self, field_name: typing.Literal["_error", b"_error", "error", b"error"]) -> builtins.bool: ...
    def ClearField(
        self, field_name: typing.Literal["_error", b"_error", "error", b"error", "success", b"success"]
    ) -> None: ...
    def WhichOneof(self, oneof_group: typing.Literal["_error", b"_error"]) -> typing.Literal["error"] | None: ...

global___SaveStateResponse = SaveStateResponse

@typing.final
class Message(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    REQUEST_FIELD_NUMBER: builtins.int
    RESPONSE_FIELD_NUMBER: builtins.int
    CLOUDEVENT_FIELD_NUMBER: builtins.int
    REGISTERAGENTTYPEREQUEST_FIELD_NUMBER: builtins.int
    REGISTERAGENTTYPERESPONSE_FIELD_NUMBER: builtins.int
    ADDSUBSCRIPTIONREQUEST_FIELD_NUMBER: builtins.int
    ADDSUBSCRIPTIONRESPONSE_FIELD_NUMBER: builtins.int
    @property
    def request(self) -> global___RpcRequest: ...
    @property
    def response(self) -> global___RpcResponse: ...
    @property
    def cloudEvent(self) -> cloudevent_pb2.CloudEvent: ...
    @property
    def registerAgentTypeRequest(self) -> global___RegisterAgentTypeRequest: ...
    @property
    def registerAgentTypeResponse(self) -> global___RegisterAgentTypeResponse: ...
    @property
    def addSubscriptionRequest(self) -> global___AddSubscriptionRequest: ...
    @property
    def addSubscriptionResponse(self) -> global___AddSubscriptionResponse: ...
    def __init__(
        self,
        *,
        request: global___RpcRequest | None = ...,
        response: global___RpcResponse | None = ...,
        cloudEvent: cloudevent_pb2.CloudEvent | None = ...,
        registerAgentTypeRequest: global___RegisterAgentTypeRequest | None = ...,
        registerAgentTypeResponse: global___RegisterAgentTypeResponse | None = ...,
        addSubscriptionRequest: global___AddSubscriptionRequest | None = ...,
        addSubscriptionResponse: global___AddSubscriptionResponse | None = ...,
    ) -> None: ...
    def HasField(
        self,
        field_name: typing.Literal[
            "addSubscriptionRequest",
            b"addSubscriptionRequest",
            "addSubscriptionResponse",
            b"addSubscriptionResponse",
            "cloudEvent",
            b"cloudEvent",
            "message",
            b"message",
            "registerAgentTypeRequest",
            b"registerAgentTypeRequest",
            "registerAgentTypeResponse",
            b"registerAgentTypeResponse",
            "request",
            b"request",
            "response",
            b"response",
        ],
    ) -> builtins.bool: ...
    def ClearField(
        self,
        field_name: typing.Literal[
            "addSubscriptionRequest",
            b"addSubscriptionRequest",
            "addSubscriptionResponse",
            b"addSubscriptionResponse",
            "cloudEvent",
            b"cloudEvent",
            "message",
            b"message",
            "registerAgentTypeRequest",
            b"registerAgentTypeRequest",
            "registerAgentTypeResponse",
            b"registerAgentTypeResponse",
            "request",
            b"request",
            "response",
            b"response",
        ],
    ) -> None: ...
    def WhichOneof(
        self, oneof_group: typing.Literal["message", b"message"]
    ) -> (
        typing.Literal[
            "request",
            "response",
            "cloudEvent",
            "registerAgentTypeRequest",
            "registerAgentTypeResponse",
            "addSubscriptionRequest",
            "addSubscriptionResponse",
        ]
        | None
    ): ...

global___Message = Message