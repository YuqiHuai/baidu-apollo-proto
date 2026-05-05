"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
_sym_db = _symbol_database.Default()
from ......modules.drivers.lidar.common.proto import lidar_config_base_pb2 as modules_dot_drivers_dot_lidar_dot_common_dot_proto_dot_lidar__config__base__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n8modules/drivers/lidar/rslidar/proto/rslidar_config.proto\x12\x18apollo.drivers.robosense\x1a:modules/drivers/lidar/common/proto/lidar_config_base.proto"\xd4\x05\n\x06Config\x12:\n\x0bconfig_base\x18! \x02(\x0b2%.apollo.drivers.lidar.LidarConfigBase\x12\r\n\x05model\x18\x01 \x01(\t\x12\n\n\x02ip\x18\x03 \x01(\t\x12\x11\n\tmsop_port\x18\x04 \x01(\r\x12\x12\n\ndifop_port\x18\x05 \x01(\r\x12\x11\n\techo_mode\x18\x06 \x01(\r\x12\x13\n\x0bstart_angle\x18\x07 \x01(\x02\x12\x11\n\tend_angle\x18\x08 \x01(\x02\x12\x14\n\x0cmin_distance\x18\t \x01(\x02\x12\x14\n\x0cmax_distance\x18\n \x01(\x02\x12\x11\n\tcut_angle\x18\x0b \x01(\x02\x12\x1e\n\x0fuse_lidar_clock\x18\x0c \x01(\x08:\x05false\x12\x19\n\x0enum_pkts_split\x18\r \x01(\r:\x010\x12\x1b\n\x10split_frame_node\x18\x0e \x01(\r:\x011\x12\x18\n\x10calibration_file\x18\x11 \x01(\t\x12\x1b\n\x0cdense_points\x18\x12 \x01(\x08:\x05false\x12\x1d\n\x0ets_first_point\x18\x13 \x01(\x08:\x05false\x12\x1c\n\x0ewait_for_difop\x18\x14 \x01(\x08:\x04true\x12\x1f\n\x10config_from_file\x18\x15 \x01(\x08:\x05false\x12\x14\n\nangle_path\x18\x16 \x01(\t:\x00\x12\x16\n\x0bsplit_angle\x18\x17 \x01(\x02:\x010\x12\x1d\n\x0chost_address\x18\x18 \x01(\t:\x070.0.0.0\x12\x1e\n\rgroup_address\x18\x19 \x01(\t:\x070.0.0.0\x12\x17\n\x08use_vlan\x18\x1a \x01(\x08:\x05false\x12\x1f\n\x10user_layer_bytes\x18\x1b \x01(\x08:\x05false\x12\x1f\n\x10tail_layer_bytes\x18\x1c \x01(\x08:\x05false\x12\x1d\n\x0fsend_raw_packet\x18\x1d \x01(\x08:\x04true')
_CONFIG = DESCRIPTOR.message_types_by_name['Config']
Config = _reflection.GeneratedProtocolMessageType('Config', (_message.Message,), {'DESCRIPTOR': _CONFIG, '__module__': 'modules.drivers.lidar.rslidar.proto.rslidar_config_pb2'})
_sym_db.RegisterMessage(Config)
if _descriptor._USE_C_DESCRIPTORS == False:
    DESCRIPTOR._options = None
    _CONFIG._serialized_start = 147
    _CONFIG._serialized_end = 871