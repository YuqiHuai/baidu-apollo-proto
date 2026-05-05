"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
_sym_db = _symbol_database.Default()
from ......modules.drivers.lidar.common.proto import lidar_config_base_pb2 as modules_dot_drivers_dot_lidar_dot_common_dot_proto_dot_lidar__config__base__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n@modules/drivers/lidar/vanjeelidar/proto/vanjeelidar_config.proto\x12\x15apollo.drivers.vanjee\x1a:modules/drivers/lidar/common/proto/lidar_config_base.proto"\xd8\x03\n\x06Config\x12:\n\x0bconfig_base\x18! \x02(\x0b2%.apollo.drivers.lidar.LidarConfigBase\x12\r\n\x05model\x18\x01 \x01(\t\x12\x14\n\x0cconnect_type\x18\x02 \x01(\r\x12\x16\n\x0ehost_msop_port\x18\x03 \x01(\r\x12\x17\n\x0flidar_msop_port\x18\x04 \x01(\r\x12\x13\n\x0bstart_angle\x18\x05 \x01(\x02\x12\x11\n\tend_angle\x18\x06 \x01(\x02\x12\x14\n\x0cmin_distance\x18\x07 \x01(\x02\x12\x14\n\x0cmax_distance\x18\x08 \x01(\x02\x12\x1e\n\x0fuse_lidar_clock\x18\t \x01(\x08:\x05false\x12\x1b\n\x0cdense_points\x18\n \x01(\x08:\x05false\x12\x1c\n\x0ewait_for_difop\x18\x0b \x01(\x08:\x04true\x12\x1f\n\x10config_from_file\x18\x0c \x01(\x08:\x05false\x12\x14\n\nangle_path\x18\r \x01(\t:\x00\x12\x17\n\x0cpublish_mode\x18\x0e \x01(\r:\x012\x12\x1d\n\x0chost_address\x18\x0f \x01(\t:\x070.0.0.0\x12\x1e\n\rlidar_address\x18\x10 \x01(\t:\x070.0.0.0')
_CONFIG = DESCRIPTOR.message_types_by_name['Config']
Config = _reflection.GeneratedProtocolMessageType('Config', (_message.Message,), {'DESCRIPTOR': _CONFIG, '__module__': 'modules.drivers.lidar.vanjeelidar.proto.vanjeelidar_config_pb2'})
_sym_db.RegisterMessage(Config)
if _descriptor._USE_C_DESCRIPTORS == False:
    DESCRIPTOR._options = None
    _CONFIG._serialized_start = 152
    _CONFIG._serialized_end = 624