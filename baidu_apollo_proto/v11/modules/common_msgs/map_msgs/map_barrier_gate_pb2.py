"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
_sym_db = _symbol_database.Default()
from ....modules.common_msgs.map_msgs import map_geometry_pb2 as modules_dot_common__msgs_dot_map__msgs_dot_map__geometry__pb2
from ....modules.common_msgs.map_msgs import map_id_pb2 as modules_dot_common__msgs_dot_map__msgs_dot_map__id__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n3modules/common_msgs/map_msgs/map_barrier_gate.proto\x12\x0capollo.hdmap\x1a/modules/common_msgs/map_msgs/map_geometry.proto\x1a)modules/common_msgs/map_msgs/map_id.proto"\xad\x02\n\x0bBarrierGate\x12\x1c\n\x02id\x18\x01 \x02(\x0b2\x10.apollo.hdmap.Id\x127\n\x04type\x18\x02 \x01(\x0e2).apollo.hdmap.BarrierGate.BarrierGateType\x12&\n\x07polygon\x18\x03 \x01(\x0b2\x15.apollo.hdmap.Polygon\x12&\n\tstop_line\x18\x04 \x03(\x0b2\x13.apollo.hdmap.Curve\x12$\n\noverlap_id\x18\x05 \x03(\x0b2\x10.apollo.hdmap.Id"Q\n\x0fBarrierGateType\x12\x07\n\x03ROD\x10\x01\x12\t\n\x05FENCE\x10\x02\x12\x0f\n\x0bADVERTISING\x10\x03\x12\x0e\n\nTELESCOPIC\x10\x04\x12\t\n\x05OTHER\x10\x05')
_BARRIERGATE = DESCRIPTOR.message_types_by_name['BarrierGate']
_BARRIERGATE_BARRIERGATETYPE = _BARRIERGATE.enum_types_by_name['BarrierGateType']
BarrierGate = _reflection.GeneratedProtocolMessageType('BarrierGate', (_message.Message,), {'DESCRIPTOR': _BARRIERGATE, '__module__': 'modules.common_msgs.map_msgs.map_barrier_gate_pb2'})
_sym_db.RegisterMessage(BarrierGate)
if _descriptor._USE_C_DESCRIPTORS == False:
    DESCRIPTOR._options = None
    _BARRIERGATE._serialized_start = 162
    _BARRIERGATE._serialized_end = 463
    _BARRIERGATE_BARRIERGATETYPE._serialized_start = 382
    _BARRIERGATE_BARRIERGATETYPE._serialized_end = 463