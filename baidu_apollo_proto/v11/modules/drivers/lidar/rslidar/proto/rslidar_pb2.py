"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
_sym_db = _symbol_database.Default()
from ......modules.common_msgs.basic_msgs import header_pb2 as modules_dot_common__msgs_dot_basic__msgs_dot_header__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n1modules/drivers/lidar/rslidar/proto/rslidar.proto\x12\x18apollo.drivers.robosense\x1a+modules/common_msgs/basic_msgs/header.proto"2\n\x13RobosenseScanPacket\x12\r\n\x05stamp\x18\x01 \x01(\x04\x12\x0c\n\x04data\x18\x02 \x01(\x0c"G\n\rRobosenseScan\x12\x10\n\x08is_difop\x18\x01 \x01(\x08\x12\x16\n\x0eis_frame_begin\x18\x02 \x01(\x08\x12\x0c\n\x04data\x18\x03 \x01(\x0c')
_ROBOSENSESCANPACKET = DESCRIPTOR.message_types_by_name['RobosenseScanPacket']
_ROBOSENSESCAN = DESCRIPTOR.message_types_by_name['RobosenseScan']
RobosenseScanPacket = _reflection.GeneratedProtocolMessageType('RobosenseScanPacket', (_message.Message,), {'DESCRIPTOR': _ROBOSENSESCANPACKET, '__module__': 'modules.drivers.lidar.rslidar.proto.rslidar_pb2'})
_sym_db.RegisterMessage(RobosenseScanPacket)
RobosenseScan = _reflection.GeneratedProtocolMessageType('RobosenseScan', (_message.Message,), {'DESCRIPTOR': _ROBOSENSESCAN, '__module__': 'modules.drivers.lidar.rslidar.proto.rslidar_pb2'})
_sym_db.RegisterMessage(RobosenseScan)
if _descriptor._USE_C_DESCRIPTORS == False:
    DESCRIPTOR._options = None
    _ROBOSENSESCANPACKET._serialized_start = 124
    _ROBOSENSESCANPACKET._serialized_end = 174
    _ROBOSENSESCAN._serialized_start = 176
    _ROBOSENSESCAN._serialized_end = 247