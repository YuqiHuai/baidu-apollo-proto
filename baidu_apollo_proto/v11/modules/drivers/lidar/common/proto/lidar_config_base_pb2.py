"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
_sym_db = _symbol_database.Default()
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n:modules/drivers/lidar/common/proto/lidar_config_base.proto\x12\x14apollo.drivers.lidar"\xac\x02\n\x0fLidarConfigBase\x12\x14\n\x0cscan_channel\x18\x01 \x02(\t\x12\x1b\n\x13point_cloud_channel\x18\x02 \x02(\t\x12\x10\n\x08frame_id\x18\x03 \x02(\t\x12E\n\x0bsource_type\x18\x04 \x02(\x0e20.apollo.drivers.lidar.LidarConfigBase.SourceType\x12\x17\n\x0bbuffer_size\x18\x05 \x01(\x05:\x0210\x12\x18\n\nwrite_scan\x18\x06 \x01(\x08:\x04true\x12*\n\x1bdefault_reserved_points_num\x18\x07 \x01(\r:\x0550000".\n\nSourceType\x12\x10\n\x0cONLINE_LIDAR\x10\x00\x12\x0e\n\nRAW_PACKET\x10\x01')
_LIDARCONFIGBASE = DESCRIPTOR.message_types_by_name['LidarConfigBase']
_LIDARCONFIGBASE_SOURCETYPE = _LIDARCONFIGBASE.enum_types_by_name['SourceType']
LidarConfigBase = _reflection.GeneratedProtocolMessageType('LidarConfigBase', (_message.Message,), {'DESCRIPTOR': _LIDARCONFIGBASE, '__module__': 'modules.drivers.lidar.common.proto.lidar_config_base_pb2'})
_sym_db.RegisterMessage(LidarConfigBase)
if _descriptor._USE_C_DESCRIPTORS == False:
    DESCRIPTOR._options = None
    _LIDARCONFIGBASE._serialized_start = 85
    _LIDARCONFIGBASE._serialized_end = 385
    _LIDARCONFIGBASE_SOURCETYPE._serialized_start = 339
    _LIDARCONFIGBASE_SOURCETYPE._serialized_end = 385