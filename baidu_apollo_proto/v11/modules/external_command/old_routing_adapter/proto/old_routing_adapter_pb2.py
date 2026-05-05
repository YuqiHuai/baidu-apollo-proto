"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
_sym_db = _symbol_database.Default()
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\nLmodules/external_command/old_routing_adapter/proto/old_routing_adapter.proto\x12\x1aapollo.old_routing_adapter"\x80\x01\n\x17OldRoutingAdapterConfig\x12\x1d\n\x15routing_request_topic\x18\x01 \x02(\t\x12!\n\x19lane_follow_command_topic\x18\x02 \x02(\t\x12#\n\x1bvalet_parking_command_topic\x18\x03 \x02(\t')
_OLDROUTINGADAPTERCONFIG = DESCRIPTOR.message_types_by_name['OldRoutingAdapterConfig']
OldRoutingAdapterConfig = _reflection.GeneratedProtocolMessageType('OldRoutingAdapterConfig', (_message.Message,), {'DESCRIPTOR': _OLDROUTINGADAPTERCONFIG, '__module__': 'modules.external_command.old_routing_adapter.proto.old_routing_adapter_pb2'})
_sym_db.RegisterMessage(OldRoutingAdapterConfig)
if _descriptor._USE_C_DESCRIPTORS == False:
    DESCRIPTOR._options = None
    _OLDROUTINGADAPTERCONFIG._serialized_start = 109
    _OLDROUTINGADAPTERCONFIG._serialized_end = 237