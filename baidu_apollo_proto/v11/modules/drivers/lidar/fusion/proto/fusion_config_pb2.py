"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
_sym_db = _symbol_database.Default()
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n6modules/drivers/lidar/fusion/proto/fusion_config.proto\x12\x15apollo.drivers.fusion"\x86\x01\n\x0cFusionConfig\x12\x17\n\x0fmax_interval_ms\x18\x01 \x01(\r\x12\x19\n\x11drop_expired_data\x18\x02 \x01(\x08\x12\x16\n\x0efusion_channel\x18\x03 \x01(\t\x12\x15\n\rinput_channel\x18\x04 \x03(\t\x12\x13\n\x0bwait_time_s\x18\x05 \x01(\x02')
_FUSIONCONFIG = DESCRIPTOR.message_types_by_name['FusionConfig']
FusionConfig = _reflection.GeneratedProtocolMessageType('FusionConfig', (_message.Message,), {'DESCRIPTOR': _FUSIONCONFIG, '__module__': 'modules.drivers.lidar.fusion.proto.fusion_config_pb2'})
_sym_db.RegisterMessage(FusionConfig)
if _descriptor._USE_C_DESCRIPTORS == False:
    DESCRIPTOR._options = None
    _FUSIONCONFIG._serialized_start = 82
    _FUSIONCONFIG._serialized_end = 216