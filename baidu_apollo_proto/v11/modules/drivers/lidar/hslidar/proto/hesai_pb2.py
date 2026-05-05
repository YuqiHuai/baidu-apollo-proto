"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
_sym_db = _symbol_database.Default()
from ......modules.common_msgs.basic_msgs import header_pb2 as modules_dot_common__msgs_dot_basic__msgs_dot_header__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n/modules/drivers/lidar/hslidar/proto/hesai.proto\x12\x14apollo.drivers.lidar\x1a+modules/common_msgs/basic_msgs/header.proto"C\n\x0eHesaiUdpPacket\x12\x15\n\rtimestamp_sec\x18\x01 \x01(\x01\x12\x0c\n\x04data\x18\x02 \x01(\x0c\x12\x0c\n\x04size\x18\x03 \x01(\r"m\n\rHesaiUdpFrame\x12%\n\x06header\x18\x01 \x01(\x0b2\x15.apollo.common.Header\x125\n\x07packets\x18\x02 \x03(\x0b2$.apollo.drivers.lidar.HesaiUdpPacket')
_HESAIUDPPACKET = DESCRIPTOR.message_types_by_name['HesaiUdpPacket']
_HESAIUDPFRAME = DESCRIPTOR.message_types_by_name['HesaiUdpFrame']
HesaiUdpPacket = _reflection.GeneratedProtocolMessageType('HesaiUdpPacket', (_message.Message,), {'DESCRIPTOR': _HESAIUDPPACKET, '__module__': 'modules.drivers.lidar.hslidar.proto.hesai_pb2'})
_sym_db.RegisterMessage(HesaiUdpPacket)
HesaiUdpFrame = _reflection.GeneratedProtocolMessageType('HesaiUdpFrame', (_message.Message,), {'DESCRIPTOR': _HESAIUDPFRAME, '__module__': 'modules.drivers.lidar.hslidar.proto.hesai_pb2'})
_sym_db.RegisterMessage(HesaiUdpFrame)
if _descriptor._USE_C_DESCRIPTORS == False:
    DESCRIPTOR._options = None
    _HESAIUDPPACKET._serialized_start = 118
    _HESAIUDPPACKET._serialized_end = 185
    _HESAIUDPFRAME._serialized_start = 187
    _HESAIUDPFRAME._serialized_end = 296