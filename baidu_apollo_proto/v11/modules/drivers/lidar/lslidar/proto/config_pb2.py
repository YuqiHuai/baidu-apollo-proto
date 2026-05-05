"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
_sym_db = _symbol_database.Default()
from ......modules.drivers.lidar.lslidar.proto import lslidar_pb2 as modules_dot_drivers_dot_lidar_dot_lslidar_dot_proto_dot_lslidar__pb2
from ......modules.drivers.lidar.common.proto import lidar_config_base_pb2 as modules_dot_drivers_dot_lidar_dot_common_dot_proto_dot_lidar__config__base__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n0modules/drivers/lidar/lslidar/proto/config.proto\x12\x16apollo.drivers.lslidar\x1a1modules/drivers/lidar/lslidar/proto/lslidar.proto\x1a:modules/drivers/lidar/common/proto/lidar_config_base.proto"\xda\x05\n\x06Config\x12:\n\x0bconfig_base\x18! \x01(\x0b2%.apollo.drivers.lidar.LidarConfigBase\x12,\n\x05model\x18\x01 \x01(\x0e2\x1d.apollo.drivers.lslidar.Model\x12 \n\tdevice_ip\x18\x02 \x01(\t:\r192.168.1.200\x12\x11\n\tmsop_port\x18\x03 \x01(\r\x12\x12\n\ndifop_port\x18\x04 \x01(\r\x12\x13\n\x0breturn_mode\x18\x05 \x01(\r\x12\x13\n\x0bdegree_mode\x18\x06 \x01(\r\x12\x15\n\rdistance_unit\x18\x07 \x01(\x02\x12\x1c\n\x14time_synchronization\x18\x08 \x01(\x08\x12\x15\n\radd_multicast\x18\t \x01(\x08\x12\x1b\n\x08group_ip\x18\n \x01(\t:\t224.1.1.2\x12\x0b\n\x03rpm\x18\x0b \x01(\r\x12\x11\n\ttime_zone\x18\r \x01(\r\x12\x10\n\x08frame_id\x18\x0e \x01(\t\x12\x11\n\tmin_range\x18\x10 \x01(\x02\x12\x11\n\tmax_range\x18\x11 \x01(\x02\x12\x13\n\x0bconfig_vert\x18\x12 \x01(\x08\x12\x12\n\nprint_vert\x18\x13 \x01(\x08\x12\x18\n\x10scan_start_angle\x18\x14 \x01(\x02\x12\x16\n\x0escan_end_angle\x18\x15 \x01(\x02\x12\x13\n\x0bcalibration\x18\x16 \x01(\x08\x12\x10\n\x08npackets\x18\x17 \x01(\x05\x12\x18\n\x10calibration_file\x18\x18 \x01(\t\x12\x13\n\x0bpacket_size\x18\x19 \x01(\r\x12\x16\n\x0evertical_angle\x18\x1a \x01(\r\x12\x15\n\rbottom_left_x\x18\x1b \x01(\x02\x12\x15\n\rbottom_left_y\x18\x1c \x01(\x02\x12\x13\n\x0btop_right_x\x18\x1d \x01(\x02\x12\x13\n\x0btop_right_y\x18\x1e \x01(\x02\x12\x11\n\tpcap_path\x18\x1f \x01(\t')
_CONFIG = DESCRIPTOR.message_types_by_name['Config']
Config = _reflection.GeneratedProtocolMessageType('Config', (_message.Message,), {'DESCRIPTOR': _CONFIG, '__module__': 'modules.drivers.lidar.lslidar.proto.config_pb2'})
_sym_db.RegisterMessage(Config)
if _descriptor._USE_C_DESCRIPTORS == False:
    DESCRIPTOR._options = None
    _CONFIG._serialized_start = 188
    _CONFIG._serialized_end = 918