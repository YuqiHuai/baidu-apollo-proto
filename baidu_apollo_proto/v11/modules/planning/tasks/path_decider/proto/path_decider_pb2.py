"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
_sym_db = _symbol_database.Default()
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n<modules/planning/tasks/path_decider/proto/path_decider.proto\x12\x0fapollo.planning"\x89\x01\n\x11PathDeciderConfig\x12#\n\x16static_obstacle_buffer\x18\x01 \x01(\x01:\x030.3\x12\'\n\x18ignore_backward_obstacle\x18\x02 \x01(\x08:\x05false\x12&\n\x17skip_overlap_stop_check\x18\x03 \x01(\x08:\x05false')
_PATHDECIDERCONFIG = DESCRIPTOR.message_types_by_name['PathDeciderConfig']
PathDeciderConfig = _reflection.GeneratedProtocolMessageType('PathDeciderConfig', (_message.Message,), {'DESCRIPTOR': _PATHDECIDERCONFIG, '__module__': 'modules.planning.tasks.path_decider.proto.path_decider_pb2'})
_sym_db.RegisterMessage(PathDeciderConfig)
if _descriptor._USE_C_DESCRIPTORS == False:
    DESCRIPTOR._options = None
    _PATHDECIDERCONFIG._serialized_start = 82
    _PATHDECIDERCONFIG._serialized_end = 219