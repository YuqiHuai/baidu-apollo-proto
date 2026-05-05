"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
_sym_db = _symbol_database.Default()
from ......modules.drivers.lidar.common.proto import lidar_config_base_pb2 as modules_dot_drivers_dot_lidar_dot_common_dot_proto_dot_lidar__config__base__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n6modules/drivers/lidar/seyond/proto/seyond_config.proto\x12\x15apollo.drivers.seyond\x1a:modules/drivers/lidar/common/proto/lidar_config_base.proto"\xb4\x02\n\x06Config\x12:\n\x0bconfig_base\x18\x01 \x02(\x0b2%.apollo.drivers.lidar.LidarConfigBase\x12\x1f\n\tdevice_ip\x18\x02 \x01(\t:\x0c172.168.1.10\x12\x12\n\x04port\x18\x03 \x01(\r:\x048010\x12\x16\n\x08udp_port\x18\x04 \x01(\x05:\x048010\x12\x1f\n\x10reflectance_mode\x18\x05 \x01(\x08:\x05false\x12\x1a\n\x0fmultiple_return\x18\x06 \x01(\r:\x010\x12\x1a\n\x0fcoordinate_mode\x18\x07 \x01(\r:\x013\x12\x17\n\tmax_range\x18\x08 \x01(\x01:\x042000\x12\x16\n\tmin_range\x18\t \x01(\x01:\x030.4\x12\x17\n\tlog_level\x18\n \x01(\t:\x04info')
_CONFIG = DESCRIPTOR.message_types_by_name['Config']
Config = _reflection.GeneratedProtocolMessageType('Config', (_message.Message,), {'DESCRIPTOR': _CONFIG, '__module__': 'modules.drivers.lidar.seyond.proto.seyond_config_pb2'})
_sym_db.RegisterMessage(Config)
if _descriptor._USE_C_DESCRIPTORS == False:
    DESCRIPTOR._options = None
    _CONFIG._serialized_start = 142
    _CONFIG._serialized_end = 450