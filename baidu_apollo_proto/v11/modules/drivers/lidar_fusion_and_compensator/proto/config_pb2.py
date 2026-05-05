"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
_sym_db = _symbol_database.Default()
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n?modules/drivers/lidar_fusion_and_compensator/proto/config.proto\x12\x14apollo.drivers.lidar"z\n\x0cFilterConfig\x12\x10\n\x08frame_id\x18\x01 \x02(\t\x12\r\n\x05max_x\x18\x02 \x01(\x02\x12\r\n\x05min_x\x18\x03 \x01(\x02\x12\r\n\x05max_y\x18\x04 \x01(\x02\x12\r\n\x05min_y\x18\x05 \x01(\x02\x12\r\n\x05max_z\x18\x06 \x01(\x02\x12\r\n\x05min_z\x18\x07 \x01(\x02"\xfc\x02\n\x1aFusionAndCompensatorConfig\x12\x17\n\x0fmax_interval_ms\x18\x01 \x01(\r\x12\x19\n\x11drop_expired_data\x18\x02 \x01(\x08\x12\x15\n\rinput_channel\x18\x03 \x03(\t\x12\x13\n\x0bwait_time_s\x18\x04 \x01(\x02\x12\x16\n\x0eoutput_channel\x18\x05 \x01(\t\x12%\n\x17transform_query_timeout\x18\x06 \x01(\x02:\x040.02\x12\x1d\n\x0eworld_frame_id\x18\x07 \x01(\t:\x05world\x12\x17\n\x0ftarget_frame_id\x18\x08 \x01(\t\x12$\n\x15rotation_compensation\x18\t \x01(\x08:\x05false\x12&\n\x18translation_compensation\x18\n \x01(\x08:\x04true\x129\n\rfilter_config\x18\x0b \x03(\x0b2".apollo.drivers.lidar.FilterConfig')
_FILTERCONFIG = DESCRIPTOR.message_types_by_name['FilterConfig']
_FUSIONANDCOMPENSATORCONFIG = DESCRIPTOR.message_types_by_name['FusionAndCompensatorConfig']
FilterConfig = _reflection.GeneratedProtocolMessageType('FilterConfig', (_message.Message,), {'DESCRIPTOR': _FILTERCONFIG, '__module__': 'modules.drivers.lidar_fusion_and_compensator.proto.config_pb2'})
_sym_db.RegisterMessage(FilterConfig)
FusionAndCompensatorConfig = _reflection.GeneratedProtocolMessageType('FusionAndCompensatorConfig', (_message.Message,), {'DESCRIPTOR': _FUSIONANDCOMPENSATORCONFIG, '__module__': 'modules.drivers.lidar_fusion_and_compensator.proto.config_pb2'})
_sym_db.RegisterMessage(FusionAndCompensatorConfig)
if _descriptor._USE_C_DESCRIPTORS == False:
    DESCRIPTOR._options = None
    _FILTERCONFIG._serialized_start = 89
    _FILTERCONFIG._serialized_end = 211
    _FUSIONANDCOMPENSATORCONFIG._serialized_start = 214
    _FUSIONANDCOMPENSATORCONFIG._serialized_end = 594