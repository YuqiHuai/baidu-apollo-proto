"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
_sym_db = _symbol_database.Default()
from ......modules.drivers.lidar.common.proto import lidar_config_base_pb2 as modules_dot_drivers_dot_lidar_dot_common_dot_proto_dot_lidar__config__base__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n-modules/drivers/lidar/livox/proto/livox.proto\x12\x14apollo.drivers.livox\x1a:modules/drivers/lidar/common/proto/lidar_config_base.proto"c\n\x0eCustomIntegral\x12\x15\n\rintegral_time\x18\x01 \x02(\x01\x12\r\n\x05min_x\x18\x02 \x01(\x01\x12\r\n\x05max_x\x18\x03 \x01(\x01\x12\r\n\x05min_y\x18\x04 \x01(\x01\x12\r\n\x05max_y\x18\x05 \x01(\x01"\x98\x02\n\x06Config\x12:\n\x0bconfig_base\x18\x01 \x02(\x0b2%.apollo.drivers.lidar.LidarConfigBase\x12\x10\n\x08lidar_ip\x18\x02 \x02(\t\x12\x1e\n\x16lidar_config_file_path\x18\x03 \x01(\t\x12\x1a\n\rintegral_time\x18\x04 \x01(\x01:\x030.1\x12%\n\x16enable_sdk_console_log\x18\x05 \x01(\x08:\x05false\x12\x1e\n\x0fuse_lidar_clock\x18\x06 \x01(\x08:\x05false\x12=\n\x0fcustom_integral\x18\x07 \x01(\x0b2$.apollo.drivers.livox.CustomIntegral"j\n\tLivoxScan\x12\x11\n\ttimestamp\x18\x01 \x01(\x04\x12\x11\n\tdata_type\x18\x02 \x01(\x05\x12\x0c\n\x04data\x18\x03 \x01(\x0c\x12\x12\n\npoint_size\x18\x04 \x01(\x05\x12\x15\n\rtime_interval\x18\x05 \x01(\x05')
_CUSTOMINTEGRAL = DESCRIPTOR.message_types_by_name['CustomIntegral']
_CONFIG = DESCRIPTOR.message_types_by_name['Config']
_LIVOXSCAN = DESCRIPTOR.message_types_by_name['LivoxScan']
CustomIntegral = _reflection.GeneratedProtocolMessageType('CustomIntegral', (_message.Message,), {'DESCRIPTOR': _CUSTOMINTEGRAL, '__module__': 'modules.drivers.lidar.livox.proto.livox_pb2'})
_sym_db.RegisterMessage(CustomIntegral)
Config = _reflection.GeneratedProtocolMessageType('Config', (_message.Message,), {'DESCRIPTOR': _CONFIG, '__module__': 'modules.drivers.lidar.livox.proto.livox_pb2'})
_sym_db.RegisterMessage(Config)
LivoxScan = _reflection.GeneratedProtocolMessageType('LivoxScan', (_message.Message,), {'DESCRIPTOR': _LIVOXSCAN, '__module__': 'modules.drivers.lidar.livox.proto.livox_pb2'})
_sym_db.RegisterMessage(LivoxScan)
if _descriptor._USE_C_DESCRIPTORS == False:
    DESCRIPTOR._options = None
    _CUSTOMINTEGRAL._serialized_start = 131
    _CUSTOMINTEGRAL._serialized_end = 230
    _CONFIG._serialized_start = 233
    _CONFIG._serialized_end = 513
    _LIVOXSCAN._serialized_start = 515
    _LIVOXSCAN._serialized_end = 621