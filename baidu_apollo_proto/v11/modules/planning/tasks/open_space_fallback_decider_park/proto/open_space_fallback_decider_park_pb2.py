"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
_sym_db = _symbol_database.Default()
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\ndmodules/planning/tasks/open_space_fallback_decider_park/proto/open_space_fallback_decider_park.proto\x12\x0fapollo.planning"\xd0\x02\n"OpenSpaceFallBackDeciderParkConfig\x12,\n!open_space_prediction_time_period\x18\x01 \x01(\x01:\x015\x121\n&open_space_fallback_collision_distance\x18\x02 \x01(\x01:\x015\x12,\n!open_space_fallback_stop_distance\x18\x03 \x01(\x01:\x012\x125\n)open_space_fallback_collision_time_buffer\x18\x04 \x01(\x01:\x0210\x12%\n\x16is_use_trajectory_pose\x18\x05 \x01(\x08:\x05false\x12\x1a\n\x0fdistance_to_obs\x18\x06 \x01(\x01:\x011\x12!\n\x15collision_check_range\x18\x07 \x01(\x01:\x0210')
_OPENSPACEFALLBACKDECIDERPARKCONFIG = DESCRIPTOR.message_types_by_name['OpenSpaceFallBackDeciderParkConfig']
OpenSpaceFallBackDeciderParkConfig = _reflection.GeneratedProtocolMessageType('OpenSpaceFallBackDeciderParkConfig', (_message.Message,), {'DESCRIPTOR': _OPENSPACEFALLBACKDECIDERPARKCONFIG, '__module__': 'modules.planning.tasks.open_space_fallback_decider_park.proto.open_space_fallback_decider_park_pb2'})
_sym_db.RegisterMessage(OpenSpaceFallBackDeciderParkConfig)
if _descriptor._USE_C_DESCRIPTORS == False:
    DESCRIPTOR._options = None
    _OPENSPACEFALLBACKDECIDERPARKCONFIG._serialized_start = 122
    _OPENSPACEFALLBACKDECIDERPARKCONFIG._serialized_end = 458