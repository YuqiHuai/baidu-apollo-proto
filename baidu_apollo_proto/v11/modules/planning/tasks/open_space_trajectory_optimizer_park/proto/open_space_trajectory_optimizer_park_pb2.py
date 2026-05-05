"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
_sym_db = _symbol_database.Default()
from ......modules.planning.planning_open_space.proto import planner_open_space_config_pb2 as modules_dot_planning_dot_planning__open__space_dot_proto_dot_planner__open__space__config__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\nlmodules/planning/tasks/open_space_trajectory_optimizer_park/proto/open_space_trajectory_optimizer_park.proto\x12\x0fapollo.planning\x1aJmodules/planning/planning_open_space/proto/planner_open_space_config.proto"\xd3\x02\n&OpenSpaceTrajectoryOptimizerParkConfig\x12/\n!enable_trajectory_optimize_thread\x18\x01 \x01(\x08:\x04true\x12U\n\x1fdual_variable_warm_start_config\x18\x02 \x01(\x0b2,.apollo.planning.DualVariableWarmStartConfig\x12I\n\x18distance_approach_config\x18\x03 \x01(\x0b2\'.apollo.planning.DistanceApproachConfig\x12V\n#iterative_anchoring_smoother_config\x18\x04 \x01(\x0b2).apollo.planning.IterativeAnchoringConfig')
_OPENSPACETRAJECTORYOPTIMIZERPARKCONFIG = DESCRIPTOR.message_types_by_name['OpenSpaceTrajectoryOptimizerParkConfig']
OpenSpaceTrajectoryOptimizerParkConfig = _reflection.GeneratedProtocolMessageType('OpenSpaceTrajectoryOptimizerParkConfig', (_message.Message,), {'DESCRIPTOR': _OPENSPACETRAJECTORYOPTIMIZERPARKCONFIG, '__module__': 'modules.planning.tasks.open_space_trajectory_optimizer_park.proto.open_space_trajectory_optimizer_park_pb2'})
_sym_db.RegisterMessage(OpenSpaceTrajectoryOptimizerParkConfig)
if _descriptor._USE_C_DESCRIPTORS == False:
    DESCRIPTOR._options = None
    _OPENSPACETRAJECTORYOPTIMIZERPARKCONFIG._serialized_start = 206
    _OPENSPACETRAJECTORYOPTIMIZERPARKCONFIG._serialized_end = 545