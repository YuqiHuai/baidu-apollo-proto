"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
_sym_db = _symbol_database.Default()
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\nZmodules/planning/tasks/open_space_fallback_decider/proto/open_space_fallback_decider.proto\x12\x0fapollo.planning"\xe6\x01\n\x1eOpenSpaceFallBackDeciderConfig\x12,\n!open_space_prediction_time_period\x18\x01 \x01(\x01:\x015\x121\n&open_space_fallback_collision_distance\x18\x02 \x01(\x01:\x015\x12,\n!open_space_fallback_stop_distance\x18\x03 \x01(\x01:\x012\x125\n)open_space_fallback_collision_time_buffer\x18\x04 \x01(\x01:\x0210')
_OPENSPACEFALLBACKDECIDERCONFIG = DESCRIPTOR.message_types_by_name['OpenSpaceFallBackDeciderConfig']
OpenSpaceFallBackDeciderConfig = _reflection.GeneratedProtocolMessageType('OpenSpaceFallBackDeciderConfig', (_message.Message,), {'DESCRIPTOR': _OPENSPACEFALLBACKDECIDERCONFIG, '__module__': 'modules.planning.tasks.open_space_fallback_decider.proto.open_space_fallback_decider_pb2'})
_sym_db.RegisterMessage(OpenSpaceFallBackDeciderConfig)
if _descriptor._USE_C_DESCRIPTORS == False:
    DESCRIPTOR._options = None
    _OPENSPACEFALLBACKDECIDERCONFIG._serialized_start = 112
    _OPENSPACEFALLBACKDECIDERCONFIG._serialized_end = 342