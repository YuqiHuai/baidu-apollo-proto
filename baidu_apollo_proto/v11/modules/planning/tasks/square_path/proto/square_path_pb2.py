"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
_sym_db = _symbol_database.Default()
from ......modules.planning.planning_base.proto import piecewise_jerk_path_config_pb2 as modules_dot_planning_dot_planning__base_dot_proto_dot_piecewise__jerk__path__config__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n:modules/planning/tasks/square_path/proto/square_path.proto\x12\x0fapollo.planning\x1aEmodules/planning/planning_base/proto/piecewise_jerk_path_config.proto"\xa8\x01\n\x10SquarePathConfig\x12\x1c\n\x14max_lateral_distance\x18\x01 \x01(\x01\x12-\n\x1fenable_road_boundary_constraint\x18\x02 \x01(\x08:\x04true\x12G\n\x15path_optimizer_config\x18\x03 \x01(\x0b2(.apollo.planning.PiecewiseJerkPathConfig')
_SQUAREPATHCONFIG = DESCRIPTOR.message_types_by_name['SquarePathConfig']
SquarePathConfig = _reflection.GeneratedProtocolMessageType('SquarePathConfig', (_message.Message,), {'DESCRIPTOR': _SQUAREPATHCONFIG, '__module__': 'modules.planning.tasks.square_path.proto.square_path_pb2'})
_sym_db.RegisterMessage(SquarePathConfig)
if _descriptor._USE_C_DESCRIPTORS == False:
    DESCRIPTOR._options = None
    _SQUAREPATHCONFIG._serialized_start = 151
    _SQUAREPATHCONFIG._serialized_end = 319