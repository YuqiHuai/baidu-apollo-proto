"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
_sym_db = _symbol_database.Default()
from ......modules.planning.planning_open_space.proto import planner_open_space_config_pb2 as modules_dot_planning_dot_planning__open__space_dot_proto_dot_planner__open__space__config__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\nTmodules/planning/tasks/open_space_path_planning/proto/open_space_path_planning.proto\x12\x0fapollo.planning\x1aJmodules/planning/planning_open_space/proto/planner_open_space_config.proto"\x86\x02\n\x1bOpenSpacePathPlanningConfig\x12)\n\x1benable_path_planning_thread\x18\x01 \x01(\x08:\x04true\x12;\n\x11warm_start_config\x18\x02 \x01(\x0b2 .apollo.planning.WarmStartConfig\x12>\n0enable_vertical_parking_last_trajectory_straight\x18\x03 \x01(\x08:\x04true\x12?\n0enable_parallel_parking_last_trajectory_straight\x18\x04 \x01(\x08:\x05false')
_OPENSPACEPATHPLANNINGCONFIG = DESCRIPTOR.message_types_by_name['OpenSpacePathPlanningConfig']
OpenSpacePathPlanningConfig = _reflection.GeneratedProtocolMessageType('OpenSpacePathPlanningConfig', (_message.Message,), {'DESCRIPTOR': _OPENSPACEPATHPLANNINGCONFIG, '__module__': 'modules.planning.tasks.open_space_path_planning.proto.open_space_path_planning_pb2'})
_sym_db.RegisterMessage(OpenSpacePathPlanningConfig)
if _descriptor._USE_C_DESCRIPTORS == False:
    DESCRIPTOR._options = None
    _OPENSPACEPATHPLANNINGCONFIG._serialized_start = 182
    _OPENSPACEPATHPLANNINGCONFIG._serialized_end = 444