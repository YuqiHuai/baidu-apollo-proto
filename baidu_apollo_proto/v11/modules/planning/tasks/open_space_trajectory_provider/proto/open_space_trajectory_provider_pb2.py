"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
_sym_db = _symbol_database.Default()
from ......modules.planning.planning_open_space.proto import planner_open_space_config_pb2 as modules_dot_planning_dot_planning__open__space_dot_proto_dot_planner__open__space__config__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n`modules/planning/tasks/open_space_trajectory_provider/proto/open_space_trajectory_provider.proto\x12\x0fapollo.planning\x1aJmodules/planning/planning_open_space/proto/planner_open_space_config.proto"\xff\x02\n!OpenSpaceTrajectoryProviderConfig\x12c\n&open_space_trajectory_optimizer_config\x18\x01 \x01(\x0b23.apollo.planning.OpenSpaceTrajectoryOptimizerConfig\x12%\n\x1aopen_space_planning_period\x18\x02 \x01(\x01:\x014\x12.\n enable_open_space_planner_thread\x18\x03 \x01(\x08:\x04true\x12=\n0open_space_trajectory_stitching_preserved_length\x18\x04 \x01(\x01:\x03inf\x12-\n"open_space_standstill_acceleration\x18\x05 \x01(\x01:\x010\x120\n%open_space_straight_trajectory_length\x18\x06 \x01(\x01:\x010"\x94\x02\n"OpenSpaceTrajectoryOptimizerConfig\x12\x14\n\x07delta_t\x18\x04 \x01(\x02:\x030.5\x12)\n\x1anear_destination_threshold\x18\x05 \x01(\x01:\x050.001\x12J\n\x19planner_open_space_config\x18\x06 \x01(\x0b2\'.apollo.planning.PlannerOpenSpaceConfig"a\n\x12TrajectorySmoother\x12 \n\x1cITERATIVE_ANCHORING_SMOOTHER\x10\x00\x12\x15\n\x11DISTANCE_APPROACH\x10\x01\x12\x12\n\x0eUSE_WARM_START\x10\x02')
_OPENSPACETRAJECTORYPROVIDERCONFIG = DESCRIPTOR.message_types_by_name['OpenSpaceTrajectoryProviderConfig']
_OPENSPACETRAJECTORYOPTIMIZERCONFIG = DESCRIPTOR.message_types_by_name['OpenSpaceTrajectoryOptimizerConfig']
_OPENSPACETRAJECTORYOPTIMIZERCONFIG_TRAJECTORYSMOOTHER = _OPENSPACETRAJECTORYOPTIMIZERCONFIG.enum_types_by_name['TrajectorySmoother']
OpenSpaceTrajectoryProviderConfig = _reflection.GeneratedProtocolMessageType('OpenSpaceTrajectoryProviderConfig', (_message.Message,), {'DESCRIPTOR': _OPENSPACETRAJECTORYPROVIDERCONFIG, '__module__': 'modules.planning.tasks.open_space_trajectory_provider.proto.open_space_trajectory_provider_pb2'})
_sym_db.RegisterMessage(OpenSpaceTrajectoryProviderConfig)
OpenSpaceTrajectoryOptimizerConfig = _reflection.GeneratedProtocolMessageType('OpenSpaceTrajectoryOptimizerConfig', (_message.Message,), {'DESCRIPTOR': _OPENSPACETRAJECTORYOPTIMIZERCONFIG, '__module__': 'modules.planning.tasks.open_space_trajectory_provider.proto.open_space_trajectory_provider_pb2'})
_sym_db.RegisterMessage(OpenSpaceTrajectoryOptimizerConfig)
if _descriptor._USE_C_DESCRIPTORS == False:
    DESCRIPTOR._options = None
    _OPENSPACETRAJECTORYPROVIDERCONFIG._serialized_start = 194
    _OPENSPACETRAJECTORYPROVIDERCONFIG._serialized_end = 577
    _OPENSPACETRAJECTORYOPTIMIZERCONFIG._serialized_start = 580
    _OPENSPACETRAJECTORYOPTIMIZERCONFIG._serialized_end = 856
    _OPENSPACETRAJECTORYOPTIMIZERCONFIG_TRAJECTORYSMOOTHER._serialized_start = 759
    _OPENSPACETRAJECTORYOPTIMIZERCONFIG_TRAJECTORYSMOOTHER._serialized_end = 856