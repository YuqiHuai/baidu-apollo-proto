"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
_sym_db = _symbol_database.Default()
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\nPmodules/planning/traffic_rules/reference_line_end/proto/reference_line_end.proto\x12\x0fapollo.planning"b\n\x16ReferenceLineEndConfig\x12\x1a\n\rstop_distance\x18\x01 \x01(\x01:\x030.5\x12,\n min_reference_line_remain_length\x18\x02 \x01(\x01:\x0250')
_REFERENCELINEENDCONFIG = DESCRIPTOR.message_types_by_name['ReferenceLineEndConfig']
ReferenceLineEndConfig = _reflection.GeneratedProtocolMessageType('ReferenceLineEndConfig', (_message.Message,), {'DESCRIPTOR': _REFERENCELINEENDCONFIG, '__module__': 'modules.planning.traffic_rules.reference_line_end.proto.reference_line_end_pb2'})
_sym_db.RegisterMessage(ReferenceLineEndConfig)
if _descriptor._USE_C_DESCRIPTORS == False:
    DESCRIPTOR._options = None
    _REFERENCELINEENDCONFIG._serialized_start = 101
    _REFERENCELINEENDCONFIG._serialized_end = 199