"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
_sym_db = _symbol_database.Default()
from ......modules.common_msgs.basic_msgs import header_pb2 as modules_dot_common__msgs_dot_basic__msgs_dot_header__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n9modules/drivers/lidar/vanjeelidar/proto/vanjeelidar.proto\x12\x15apollo.drivers.vanjee\x1a+modules/common_msgs/basic_msgs/header.proto"/\n\x10VanjeeScanPacket\x12\r\n\x05stamp\x18\x01 \x01(\x04\x12\x0c\n\x04data\x18\x02 \x01(\x0c"D\n\nVanjeeScan\x12\x10\n\x08is_difop\x18\x01 \x01(\x08\x12\x16\n\x0eis_frame_begin\x18\x02 \x01(\x08\x12\x0c\n\x04data\x18\x03 \x01(\x0c')
_VANJEESCANPACKET = DESCRIPTOR.message_types_by_name['VanjeeScanPacket']
_VANJEESCAN = DESCRIPTOR.message_types_by_name['VanjeeScan']
VanjeeScanPacket = _reflection.GeneratedProtocolMessageType('VanjeeScanPacket', (_message.Message,), {'DESCRIPTOR': _VANJEESCANPACKET, '__module__': 'modules.drivers.lidar.vanjeelidar.proto.vanjeelidar_pb2'})
_sym_db.RegisterMessage(VanjeeScanPacket)
VanjeeScan = _reflection.GeneratedProtocolMessageType('VanjeeScan', (_message.Message,), {'DESCRIPTOR': _VANJEESCAN, '__module__': 'modules.drivers.lidar.vanjeelidar.proto.vanjeelidar_pb2'})
_sym_db.RegisterMessage(VanjeeScan)
if _descriptor._USE_C_DESCRIPTORS == False:
    DESCRIPTOR._options = None
    _VANJEESCANPACKET._serialized_start = 129
    _VANJEESCANPACKET._serialized_end = 176
    _VANJEESCAN._serialized_start = 178
    _VANJEESCAN._serialized_end = 246