"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
_sym_db = _symbol_database.Default()
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\nBmodules/planning/traffic_rules/destination/proto/destination.proto\x12\x0fapollo.planning"/\n\x11DestinationConfig\x12\x1a\n\rstop_distance\x18\x01 \x01(\x01:\x030.5')
_DESTINATIONCONFIG = DESCRIPTOR.message_types_by_name['DestinationConfig']
DestinationConfig = _reflection.GeneratedProtocolMessageType('DestinationConfig', (_message.Message,), {'DESCRIPTOR': _DESTINATIONCONFIG, '__module__': 'modules.planning.traffic_rules.destination.proto.destination_pb2'})
_sym_db.RegisterMessage(DestinationConfig)
if _descriptor._USE_C_DESCRIPTORS == False:
    DESCRIPTOR._options = None
    _DESTINATIONCONFIG._serialized_start = 87
    _DESTINATIONCONFIG._serialized_end = 134