"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
_sym_db = _symbol_database.Default()
from ....modules.common_msgs.basic_msgs import header_pb2 as modules_dot_common__msgs_dot_basic__msgs_dot_header__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\nAmodules/common_msgs/perception_msgs/perception_barrier_gate.proto\x12\x11apollo.perception\x1a+modules/common_msgs/basic_msgs/header.proto"\xd8\x01\n\x0bBarrierGate\x125\n\x06status\x18\x01 \x01(\x0e2%.apollo.perception.BarrierGate.Status\x12\n\n\x02id\x18\x02 \x01(\t\x12\x0c\n\x04type\x18\x03 \x01(\t\x12\x19\n\nis_useable\x18\x04 \x01(\x08:\x05false\x12\x14\n\x0copen_percent\x18\x05 \x01(\x01"G\n\x06Status\x12\x0b\n\x07UNKNOWN\x10\x00\x12\n\n\x06CLOSED\x10\x01\x12\x0b\n\x07CLOSING\x10\x02\x12\n\n\x06OPENED\x10\x03\x12\x0b\n\x07OPENING\x10\x04"u\n\x15PerceptionBarrierGate\x12%\n\x06header\x18\x01 \x01(\x0b2\x15.apollo.common.Header\x125\n\rbarrier_gates\x18\x02 \x03(\x0b2\x1e.apollo.perception.BarrierGate')
_BARRIERGATE = DESCRIPTOR.message_types_by_name['BarrierGate']
_PERCEPTIONBARRIERGATE = DESCRIPTOR.message_types_by_name['PerceptionBarrierGate']
_BARRIERGATE_STATUS = _BARRIERGATE.enum_types_by_name['Status']
BarrierGate = _reflection.GeneratedProtocolMessageType('BarrierGate', (_message.Message,), {'DESCRIPTOR': _BARRIERGATE, '__module__': 'modules.common_msgs.perception_msgs.perception_barrier_gate_pb2'})
_sym_db.RegisterMessage(BarrierGate)
PerceptionBarrierGate = _reflection.GeneratedProtocolMessageType('PerceptionBarrierGate', (_message.Message,), {'DESCRIPTOR': _PERCEPTIONBARRIERGATE, '__module__': 'modules.common_msgs.perception_msgs.perception_barrier_gate_pb2'})
_sym_db.RegisterMessage(PerceptionBarrierGate)
if _descriptor._USE_C_DESCRIPTORS == False:
    DESCRIPTOR._options = None
    _BARRIERGATE._serialized_start = 134
    _BARRIERGATE._serialized_end = 350
    _BARRIERGATE_STATUS._serialized_start = 279
    _BARRIERGATE_STATUS._serialized_end = 350
    _PERCEPTIONBARRIERGATE._serialized_start = 352
    _PERCEPTIONBARRIERGATE._serialized_end = 469