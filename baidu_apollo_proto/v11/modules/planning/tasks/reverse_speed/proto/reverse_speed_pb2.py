"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
_sym_db = _symbol_database.Default()
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n>modules/planning/tasks/reverse_speed/proto/reverse_speed.proto\x12\x0fapollo.planning"q\n\x12ReverseSpeedConfig\x12\x16\n\x0bspeed_limit\x18\x01 \x01(\x01:\x011\x12\x15\n\ntotal_time\x18\x02 \x01(\x01:\x018\x12\x15\n\x08l_buffer\x18\x03 \x01(\x01:\x030.2\x12\x15\n\x08s_buffer\x18\x04 \x01(\x01:\x030.2')
_REVERSESPEEDCONFIG = DESCRIPTOR.message_types_by_name['ReverseSpeedConfig']
ReverseSpeedConfig = _reflection.GeneratedProtocolMessageType('ReverseSpeedConfig', (_message.Message,), {'DESCRIPTOR': _REVERSESPEEDCONFIG, '__module__': 'modules.planning.tasks.reverse_speed.proto.reverse_speed_pb2'})
_sym_db.RegisterMessage(ReverseSpeedConfig)
if _descriptor._USE_C_DESCRIPTORS == False:
    DESCRIPTOR._options = None
    _REVERSESPEEDCONFIG._serialized_start = 83
    _REVERSESPEEDCONFIG._serialized_end = 196