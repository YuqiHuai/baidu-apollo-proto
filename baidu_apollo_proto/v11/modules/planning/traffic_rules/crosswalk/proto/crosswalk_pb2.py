"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
_sym_db = _symbol_database.Default()
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n>modules/planning/traffic_rules/crosswalk/proto/crosswalk.proto\x12\x0fapollo.planning"\x92\x02\n\x0fCrosswalkConfig\x12\x18\n\rstop_distance\x18\x01 \x01(\x01:\x011\x12 \n\x15max_stop_deceleration\x18\x02 \x01(\x01:\x014\x12\x1e\n\x13min_pass_s_distance\x18\x03 \x01(\x01:\x011\x12\x1c\n\x11expand_s_distance\x18\x05 \x01(\x01:\x012\x12!\n\x16stop_strict_l_distance\x18\x06 \x01(\x01:\x014\x12 \n\x15stop_loose_l_distance\x18\x07 \x01(\x01:\x015\x12\x18\n\x0cstop_timeout\x18\x08 \x01(\x01:\x0210\x12&\n\x1astart_watch_timer_distance\x18\t \x01(\x01:\x0240')
_CROSSWALKCONFIG = DESCRIPTOR.message_types_by_name['CrosswalkConfig']
CrosswalkConfig = _reflection.GeneratedProtocolMessageType('CrosswalkConfig', (_message.Message,), {'DESCRIPTOR': _CROSSWALKCONFIG, '__module__': 'modules.planning.traffic_rules.crosswalk.proto.crosswalk_pb2'})
_sym_db.RegisterMessage(CrosswalkConfig)
if _descriptor._USE_C_DESCRIPTORS == False:
    DESCRIPTOR._options = None
    _CROSSWALKCONFIG._serialized_start = 84
    _CROSSWALKCONFIG._serialized_end = 358