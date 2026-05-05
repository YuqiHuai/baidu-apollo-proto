"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
_sym_db = _symbol_database.Default()
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n@modules/drivers/lidar/compensator/proto/compensator_config.proto\x12\x1aapollo.drivers.compensator"\xa4\x01\n\x11CompensatorConfig\x12\x16\n\x0eoutput_channel\x18\x01 \x01(\t\x12%\n\x17transform_query_timeout\x18\x02 \x01(\x02:\x040.02\x12\x1d\n\x0eworld_frame_id\x18\x03 \x01(\t:\x05world\x12\x17\n\x0ftarget_frame_id\x18\x04 \x01(\t\x12\x18\n\x10point_cloud_size\x18\x05 \x01(\r')
_COMPENSATORCONFIG = DESCRIPTOR.message_types_by_name['CompensatorConfig']
CompensatorConfig = _reflection.GeneratedProtocolMessageType('CompensatorConfig', (_message.Message,), {'DESCRIPTOR': _COMPENSATORCONFIG, '__module__': 'modules.drivers.lidar.compensator.proto.compensator_config_pb2'})
_sym_db.RegisterMessage(CompensatorConfig)
if _descriptor._USE_C_DESCRIPTORS == False:
    DESCRIPTOR._options = None
    _COMPENSATORCONFIG._serialized_start = 97
    _COMPENSATORCONFIG._serialized_end = 261