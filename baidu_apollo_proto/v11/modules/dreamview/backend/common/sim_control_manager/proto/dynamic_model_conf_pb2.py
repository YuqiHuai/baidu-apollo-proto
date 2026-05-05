"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
_sym_db = _symbol_database.Default()
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\nSmodules/dreamview/backend/common/sim_control_manager/proto/dynamic_model_conf.proto\x12\x10apollo.dreamview"\x7f\n\x10DynamicModelConf\x12\x1a\n\x12dynamic_model_name\x18\x01 \x01(\t\x12\x14\n\x0clibrary_name\x18\x02 \x01(\t\x12\x1b\n\x13dynamic_model_files\x18\x03 \x03(\t\x12\x1c\n\x14depend_model_package\x18\x04 \x01(\t')
_DYNAMICMODELCONF = DESCRIPTOR.message_types_by_name['DynamicModelConf']
DynamicModelConf = _reflection.GeneratedProtocolMessageType('DynamicModelConf', (_message.Message,), {'DESCRIPTOR': _DYNAMICMODELCONF, '__module__': 'modules.dreamview.backend.common.sim_control_manager.proto.dynamic_model_conf_pb2'})
_sym_db.RegisterMessage(DynamicModelConf)
if _descriptor._USE_C_DESCRIPTORS == False:
    DESCRIPTOR._options = None
    _DYNAMICMODELCONF._serialized_start = 105
    _DYNAMICMODELCONF._serialized_end = 232