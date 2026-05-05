"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
_sym_db = _symbol_database.Default()
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n>modules/planning/traffic_rules/keepclear/proto/keepclear.proto\x12\x0fapollo.planning"\xa6\x01\n\x0fKeepClearConfig\x12$\n\x16enable_keep_clear_zone\x18\x01 \x01(\x08:\x04true\x12\x1d\n\x0fenable_junction\x18\x02 \x01(\x08:\x04true\x12\x1e\n\x13min_pass_s_distance\x18\x03 \x01(\x01:\x012\x12.\n!align_with_traffic_sign_tolerance\x18\x04 \x01(\x01:\x034.5')
_KEEPCLEARCONFIG = DESCRIPTOR.message_types_by_name['KeepClearConfig']
KeepClearConfig = _reflection.GeneratedProtocolMessageType('KeepClearConfig', (_message.Message,), {'DESCRIPTOR': _KEEPCLEARCONFIG, '__module__': 'modules.planning.traffic_rules.keepclear.proto.keepclear_pb2'})
_sym_db.RegisterMessage(KeepClearConfig)
if _descriptor._USE_C_DESCRIPTORS == False:
    DESCRIPTOR._options = None
    _KEEPCLEARCONFIG._serialized_start = 84
    _KEEPCLEARCONFIG._serialized_end = 250