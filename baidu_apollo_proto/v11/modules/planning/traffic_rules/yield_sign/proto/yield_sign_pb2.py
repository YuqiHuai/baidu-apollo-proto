"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
_sym_db = _symbol_database.Default()
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n@modules/planning/traffic_rules/yield_sign/proto/yield_sign.proto\x12\x0fapollo.planning"B\n\x0fYieldSignConfig\x12\x15\n\x07enabled\x18\x01 \x01(\x08:\x04true\x12\x18\n\rstop_distance\x18\x02 \x01(\x01:\x011')
_YIELDSIGNCONFIG = DESCRIPTOR.message_types_by_name['YieldSignConfig']
YieldSignConfig = _reflection.GeneratedProtocolMessageType('YieldSignConfig', (_message.Message,), {'DESCRIPTOR': _YIELDSIGNCONFIG, '__module__': 'modules.planning.traffic_rules.yield_sign.proto.yield_sign_pb2'})
_sym_db.RegisterMessage(YieldSignConfig)
if _descriptor._USE_C_DESCRIPTORS == False:
    DESCRIPTOR._options = None
    _YIELDSIGNCONFIG._serialized_start = 85
    _YIELDSIGNCONFIG._serialized_end = 151