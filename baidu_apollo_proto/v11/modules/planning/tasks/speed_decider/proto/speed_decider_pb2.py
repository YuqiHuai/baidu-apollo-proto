"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
_sym_db = _symbol_database.Default()
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n>modules/planning/tasks/speed_decider/proto/speed_decider.proto\x12\x0fapollo.planning"\x8b\x03\n\x12SpeedDeciderConfig\x12,\n\x1ffollow_min_obs_lateral_distance\x18\x01 \x01(\x01:\x032.5\x12\x1e\n\x13follow_min_time_sec\x18\x02 \x01(\x01:\x012\x12%\n\x16is_stop_for_pedestrain\x18\x03 \x01(\x08:\x05false\x12(\n\x1bkeep_clear_last_point_speed\x18\x04 \x01(\x01:\x030.8\x12\x1f\n\x14overtake_time_buffer\x18\x05 \x01(\x01:\x013\x12!\n\x15overtake_min_distance\x18\x06 \x01(\x01:\x0210\x12 \n\x15yield_distance_buffer\x18\x07 \x01(\x01:\x015\x12\x1f\n\x14stop_follow_distance\x18\x08 \x01(\x01:\x012\x12O\n\x19follow_distance_scheduler\x18\t \x01(\x0b2,.apollo.planning.FollowDistanceSchedulerInfo"W\n\x1bFollowDistanceSchedulerInfo\x128\n\x0ffollow_distance\x18\x01 \x03(\x0b2\x1f.apollo.planning.FollowDistance".\n\x0eFollowDistance\x12\r\n\x05speed\x18\x01 \x01(\x01\x12\r\n\x05slope\x18\x02 \x01(\x01')
_SPEEDDECIDERCONFIG = DESCRIPTOR.message_types_by_name['SpeedDeciderConfig']
_FOLLOWDISTANCESCHEDULERINFO = DESCRIPTOR.message_types_by_name['FollowDistanceSchedulerInfo']
_FOLLOWDISTANCE = DESCRIPTOR.message_types_by_name['FollowDistance']
SpeedDeciderConfig = _reflection.GeneratedProtocolMessageType('SpeedDeciderConfig', (_message.Message,), {'DESCRIPTOR': _SPEEDDECIDERCONFIG, '__module__': 'modules.planning.tasks.speed_decider.proto.speed_decider_pb2'})
_sym_db.RegisterMessage(SpeedDeciderConfig)
FollowDistanceSchedulerInfo = _reflection.GeneratedProtocolMessageType('FollowDistanceSchedulerInfo', (_message.Message,), {'DESCRIPTOR': _FOLLOWDISTANCESCHEDULERINFO, '__module__': 'modules.planning.tasks.speed_decider.proto.speed_decider_pb2'})
_sym_db.RegisterMessage(FollowDistanceSchedulerInfo)
FollowDistance = _reflection.GeneratedProtocolMessageType('FollowDistance', (_message.Message,), {'DESCRIPTOR': _FOLLOWDISTANCE, '__module__': 'modules.planning.tasks.speed_decider.proto.speed_decider_pb2'})
_sym_db.RegisterMessage(FollowDistance)
if _descriptor._USE_C_DESCRIPTORS == False:
    DESCRIPTOR._options = None
    _SPEEDDECIDERCONFIG._serialized_start = 84
    _SPEEDDECIDERCONFIG._serialized_end = 479
    _FOLLOWDISTANCESCHEDULERINFO._serialized_start = 481
    _FOLLOWDISTANCESCHEDULERINFO._serialized_end = 568
    _FOLLOWDISTANCE._serialized_start = 570
    _FOLLOWDISTANCE._serialized_end = 616