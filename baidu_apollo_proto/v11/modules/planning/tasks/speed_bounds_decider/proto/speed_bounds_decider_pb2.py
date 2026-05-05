"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
_sym_db = _symbol_database.Default()
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\nLmodules/planning/tasks/speed_bounds_decider/proto/speed_bounds_decider.proto\x12\x0fapollo.planning"\xb8\x03\n\x18SpeedBoundsDeciderConfig\x12\x15\n\ntotal_time\x18\x01 \x01(\x01:\x017\x12\x1c\n\x0fboundary_buffer\x18\x02 \x01(\x01:\x030.1\x12)\n\x1emax_centric_acceleration_limit\x18\x03 \x01(\x01:\x012\x12\x1c\n\rminimal_kappa\x18\x04 \x01(\x01:\x051e-05\x12\x1a\n\x0fpoint_extension\x18\x05 \x01(\x01:\x011\x12\x19\n\x0clowest_speed\x18\x06 \x01(\x01:\x032.5\x12!\n\x16collision_safety_range\x18\x07 \x01(\x01:\x011\x12$\n\x1cstatic_obs_nudge_speed_ratio\x18\x08 \x01(\x01\x12%\n\x1ddynamic_obs_nudge_speed_ratio\x18\t \x01(\x01\x12#\n\x15enable_nudge_slowdown\x18\n \x01(\x08:\x04true\x120\n#lane_change_obstacle_nudge_l_buffer\x18\x0b \x01(\x01:\x030.3\x12 \n\x12max_trajectory_len\x18\x0c \x01(\x01:\x041000')
_SPEEDBOUNDSDECIDERCONFIG = DESCRIPTOR.message_types_by_name['SpeedBoundsDeciderConfig']
SpeedBoundsDeciderConfig = _reflection.GeneratedProtocolMessageType('SpeedBoundsDeciderConfig', (_message.Message,), {'DESCRIPTOR': _SPEEDBOUNDSDECIDERCONFIG, '__module__': 'modules.planning.tasks.speed_bounds_decider.proto.speed_bounds_decider_pb2'})
_sym_db.RegisterMessage(SpeedBoundsDeciderConfig)
if _descriptor._USE_C_DESCRIPTORS == False:
    DESCRIPTOR._options = None
    _SPEEDBOUNDSDECIDERCONFIG._serialized_start = 98
    _SPEEDBOUNDSDECIDERCONFIG._serialized_end = 538