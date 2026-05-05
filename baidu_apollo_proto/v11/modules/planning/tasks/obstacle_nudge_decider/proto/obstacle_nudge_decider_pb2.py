"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
_sym_db = _symbol_database.Default()
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\nPmodules/planning/tasks/obstacle_nudge_decider/proto/obstacle_nudge_decider.proto\x12\x0fapollo.planning"\xbc\x03\n\x1aObstacleNudgeDeciderConfig\x12\x1f\n\x17enbale_nugde_static_obs\x18\x01 \x01(\x08\x12 \n\x18enbale_nugde_dynamic_obs\x18\x02 \x01(\x08\x12\x1d\n\x15min_forward_check_dis\x18\x03 \x01(\x01\x12\x1d\n\x15max_forward_check_dis\x18\x04 \x01(\x01\x12"\n\x1amax_lateral_left_nudge_dis\x18\x05 \x01(\x01\x12#\n\x1bmax_lateral_right_nudge_dis\x18\x06 \x01(\x01\x12\x1d\n\x15expand_polygon_buffer\x18\x07 \x01(\x01\x12\x1b\n\x13obs_passable_buffer\x18\x08 \x01(\x01\x12$\n\x1cobs_nudge_time_out_threshold\x18\t \x01(\x01\x12$\n\x1cobs_clean_time_out_threshold\x18\n \x01(\x01\x12\x19\n\x11full_nudge_buffer\x18\x0b \x01(\x01\x121\n)nudge_key_point_extend_length_coefficient\x18\x0c \x01(\x01')
_OBSTACLENUDGEDECIDERCONFIG = DESCRIPTOR.message_types_by_name['ObstacleNudgeDeciderConfig']
ObstacleNudgeDeciderConfig = _reflection.GeneratedProtocolMessageType('ObstacleNudgeDeciderConfig', (_message.Message,), {'DESCRIPTOR': _OBSTACLENUDGEDECIDERCONFIG, '__module__': 'modules.planning.tasks.obstacle_nudge_decider.proto.obstacle_nudge_decider_pb2'})
_sym_db.RegisterMessage(ObstacleNudgeDeciderConfig)
if _descriptor._USE_C_DESCRIPTORS == False:
    DESCRIPTOR._options = None
    _OBSTACLENUDGEDECIDERCONFIG._serialized_start = 102
    _OBSTACLENUDGEDECIDERCONFIG._serialized_end = 546