"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
_sym_db = _symbol_database.Default()
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\nbmodules/planning/planning_base/learning_based/model_inference/proto/learning_model_inference.proto\x12\x0fapollo.planning"\xde\x02\n LearningModelInferenceTaskConfig\x12O\n\nmodel_type\x18\x01 \x01(\x0e2;.apollo.planning.LearningModelInferenceTaskConfig.ModelType\x12\x16\n\x0ecpu_model_file\x18\x02 \x01(\t\x12\x16\n\x0egpu_model_file\x18\x03 \x01(\t\x12\x16\n\x08use_cuda\x18\x04 \x01(\x08:\x04true\x12\x1f\n\x12trajectory_delta_t\x18\x05 \x01(\x01:\x030.2\x12.\n\x1fallow_empty_learning_based_data\x18\x06 \x01(\x08:\x05false\x12,\n\x1dallow_empty_output_trajectory\x18\x07 \x01(\x08:\x05false""\n\tModelType\x12\x07\n\x03CNN\x10\x01\x12\x0c\n\x08CNN_LSTM\x10\x02')
_LEARNINGMODELINFERENCETASKCONFIG = DESCRIPTOR.message_types_by_name['LearningModelInferenceTaskConfig']
_LEARNINGMODELINFERENCETASKCONFIG_MODELTYPE = _LEARNINGMODELINFERENCETASKCONFIG.enum_types_by_name['ModelType']
LearningModelInferenceTaskConfig = _reflection.GeneratedProtocolMessageType('LearningModelInferenceTaskConfig', (_message.Message,), {'DESCRIPTOR': _LEARNINGMODELINFERENCETASKCONFIG, '__module__': 'modules.planning.planning_base.learning_based.model_inference.proto.learning_model_inference_pb2'})
_sym_db.RegisterMessage(LearningModelInferenceTaskConfig)
if _descriptor._USE_C_DESCRIPTORS == False:
    DESCRIPTOR._options = None
    _LEARNINGMODELINFERENCETASKCONFIG._serialized_start = 120
    _LEARNINGMODELINFERENCETASKCONFIG._serialized_end = 470
    _LEARNINGMODELINFERENCETASKCONFIG_MODELTYPE._serialized_start = 436
    _LEARNINGMODELINFERENCETASKCONFIG_MODELTYPE._serialized_end = 470