"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
_sym_db = _symbol_database.Default()
from ......modules.drivers.lidar.hslidar.proto import hesai_pb2 as modules_dot_drivers_dot_lidar_dot_hslidar_dot_proto_dot_hesai__pb2
from ......modules.drivers.lidar.common.proto import lidar_config_base_pb2 as modules_dot_drivers_dot_lidar_dot_common_dot_proto_dot_lidar__config__base__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n6modules/drivers/lidar/hslidar/proto/hesai_config.proto\x12\x14apollo.drivers.lidar\x1a/modules/drivers/lidar/hslidar/proto/hesai.proto\x1a:modules/drivers/lidar/common/proto/lidar_config_base.proto"\x83\x03\n\x0bHesaiConfig\x12:\n\x0bconfig_base\x18! \x02(\x0b2%.apollo.drivers.lidar.LidarConfigBase\x12\x13\n\x0bworker_nums\x18\x04 \x01(\x05\x12\x16\n\x08udp_port\x18\x05 \x01(\r:\x042368\x12\x16\n\x08ptc_port\x18\x06 \x01(\r:\x049347\x12 \n\tdevice_ip\x18\x07 \x01(\t:\r192.168.1.201\x12\x18\n\x07host_ip\x18\x08 \x01(\t:\x070.0.0.0\x12\x13\n\tpcap_path\x18\t \x01(\t:\x00\x12\x1c\n\x14correction_file_path\x18\n \x01(\t\x12\x16\n\x0efiretimes_path\x18\x0b \x01(\t\x12\x13\n\x0bsource_type\x18\x0c \x01(\r\x12\x1f\n\x13frame_start_azimuth\x18\r \x01(\x05:\x02-1\x12\x1b\n\x13convert_thread_nums\x18\x0e \x01(\x05\x12\x19\n\nlidar_type\x18\x0f \x01(\t:\x05AT128')
_HESAICONFIG = DESCRIPTOR.message_types_by_name['HesaiConfig']
HesaiConfig = _reflection.GeneratedProtocolMessageType('HesaiConfig', (_message.Message,), {'DESCRIPTOR': _HESAICONFIG, '__module__': 'modules.drivers.lidar.hslidar.proto.hesai_config_pb2'})
_sym_db.RegisterMessage(HesaiConfig)
if _descriptor._USE_C_DESCRIPTORS == False:
    DESCRIPTOR._options = None
    _HESAICONFIG._serialized_start = 190
    _HESAICONFIG._serialized_end = 577