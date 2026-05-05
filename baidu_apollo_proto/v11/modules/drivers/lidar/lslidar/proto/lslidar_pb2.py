"""Generated protocol buffer code."""
from google.protobuf.internal import enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
_sym_db = _symbol_database.Default()
from ......modules.common_msgs.basic_msgs import header_pb2 as modules_dot_common__msgs_dot_basic__msgs_dot_header__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n1modules/drivers/lidar/lslidar/proto/lslidar.proto\x12\x16apollo.drivers.lslidar\x1a+modules/common_msgs/basic_msgs/header.proto",\n\rLslidarPacket\x12\r\n\x05stamp\x18\x01 \x01(\x04\x12\x0c\n\x04data\x18\x02 \x01(\x0c"\xfa\x01\n\x0bLslidarScan\x12%\n\x06header\x18\x01 \x01(\x0b2\x15.apollo.common.Header\x12,\n\x05model\x18\x02 \x01(\x0e2\x1d.apollo.drivers.lslidar.Model\x12:\n\x0bfiring_pkts\x18\x03 \x03(\x0b2%.apollo.drivers.lslidar.LslidarPacket\x129\n\ndifop_pkts\x18\x04 \x03(\x0b2%.apollo.drivers.lslidar.LslidarPacket\x12\n\n\x02sn\x18\x05 \x01(\t\x12\x13\n\x08basetime\x18\x06 \x01(\x04:\x010*\xaa\x02\n\x05Model\x12\n\n\x06UNKOWN\x10\x00\x12\x0e\n\nLSLIDAR16P\x10\x01\x12\x0e\n\nLSLIDAR32P\x10\x02\x12\x0e\n\nLSLIDAR401\x10\x03\x12\x10\n\x0cLSLIDAR_CH16\x10\x04\x12\x10\n\x0cLSLIDAR_CH32\x10\x05\x12\x10\n\x0cLSLIDAR_CH64\x10\x06\x12\x11\n\rLSLIDAR_CH64w\x10\x07\x12\x11\n\rLSLIDAR_CH120\x10\x08\x12\x11\n\rLSLIDAR_CH128\x10\t\x12\x13\n\x0fLSLIDAR_CH128X1\x10\n\x12\x12\n\x0eLSLIDAR_C32_V4\x10\x0b\x12\x12\n\x0eLSLIDAR_C16_V4\x10\x0c\x12\x11\n\rLSLIDAR_C8_V4\x10\r\x12\x11\n\rLSLIDAR_C1_V4\x10\x0e\x12\x13\n\x0fLSLIDAR_LS128S2\x10\x0f')
_MODEL = DESCRIPTOR.enum_types_by_name['Model']
Model = enum_type_wrapper.EnumTypeWrapper(_MODEL)
UNKOWN = 0
LSLIDAR16P = 1
LSLIDAR32P = 2
LSLIDAR401 = 3
LSLIDAR_CH16 = 4
LSLIDAR_CH32 = 5
LSLIDAR_CH64 = 6
LSLIDAR_CH64w = 7
LSLIDAR_CH120 = 8
LSLIDAR_CH128 = 9
LSLIDAR_CH128X1 = 10
LSLIDAR_C32_V4 = 11
LSLIDAR_C16_V4 = 12
LSLIDAR_C8_V4 = 13
LSLIDAR_C1_V4 = 14
LSLIDAR_LS128S2 = 15
_LSLIDARPACKET = DESCRIPTOR.message_types_by_name['LslidarPacket']
_LSLIDARSCAN = DESCRIPTOR.message_types_by_name['LslidarScan']
LslidarPacket = _reflection.GeneratedProtocolMessageType('LslidarPacket', (_message.Message,), {'DESCRIPTOR': _LSLIDARPACKET, '__module__': 'modules.drivers.lidar.lslidar.proto.lslidar_pb2'})
_sym_db.RegisterMessage(LslidarPacket)
LslidarScan = _reflection.GeneratedProtocolMessageType('LslidarScan', (_message.Message,), {'DESCRIPTOR': _LSLIDARSCAN, '__module__': 'modules.drivers.lidar.lslidar.proto.lslidar_pb2'})
_sym_db.RegisterMessage(LslidarScan)
if _descriptor._USE_C_DESCRIPTORS == False:
    DESCRIPTOR._options = None
    _MODEL._serialized_start = 422
    _MODEL._serialized_end = 720
    _LSLIDARPACKET._serialized_start = 122
    _LSLIDARPACKET._serialized_end = 166
    _LSLIDARSCAN._serialized_start = 169
    _LSLIDARSCAN._serialized_end = 419