"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
_sym_db = _symbol_database.Default()
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n:modules/planning/planning_base/proto/planning_config.proto\x12\x0fapollo.planning"\xba\x03\n\x0bTopicConfig\x12\x15\n\rchassis_topic\x18\x01 \x01(\t\x12\x18\n\x10hmi_status_topic\x18\x02 \x01(\t\x12\x1a\n\x12localization_topic\x18\x03 \x01(\t\x12\x1a\n\x12planning_pad_topic\x18\x04 \x01(\t\x12!\n\x19planning_trajectory_topic\x18\x05 \x01(\t\x12\x18\n\x10prediction_topic\x18\x06 \x01(\t\x12\x1a\n\x12relative_map_topic\x18\x07 \x01(\t\x12\x1d\n\x15routing_request_topic\x18\x08 \x01(\t\x12\x1e\n\x16routing_response_topic\x18\t \x01(\t\x12\x1b\n\x13story_telling_topic\x18\n \x01(\t\x12%\n\x1dtraffic_light_detection_topic\x18\x0b \x01(\t\x12$\n\x1cplanning_learning_data_topic\x18\x0c \x01(\t\x12\x1e\n\x16planning_command_topic\x18\r \x01(\t\x12 \n\x18control_interative_topic\x18\x0e \x01(\t",\n\x13ReferenceLineConfig\x12\x15\n\rpnc_map_class\x18\x02 \x03(\t"\xd1\x02\n\x0ePlanningConfig\x122\n\x0ctopic_config\x18\x01 \x01(\x0b2\x1c.apollo.planning.TopicConfig\x12K\n\rlearning_mode\x18\x02 \x01(\x0e24.apollo.planning.PlanningConfig.PlanningLearningMode\x12C\n\x15reference_line_config\x18\x03 \x01(\x0b2$.apollo.planning.ReferenceLineConfig\x12\x0f\n\x07planner\x18\x04 \x01(\t"h\n\x14PlanningLearningMode\x12\x0f\n\x0bNO_LEARNING\x10\x00\x12\x07\n\x03E2E\x10\x01\x12\n\n\x06HYBRID\x10\x02\x12\x0b\n\x07RL_TEST\x10\x03\x12\x0c\n\x08E2E_TEST\x10\x04\x12\x0f\n\x0bHYBRID_TEST\x10\x05')
_TOPICCONFIG = DESCRIPTOR.message_types_by_name['TopicConfig']
_REFERENCELINECONFIG = DESCRIPTOR.message_types_by_name['ReferenceLineConfig']
_PLANNINGCONFIG = DESCRIPTOR.message_types_by_name['PlanningConfig']
_PLANNINGCONFIG_PLANNINGLEARNINGMODE = _PLANNINGCONFIG.enum_types_by_name['PlanningLearningMode']
TopicConfig = _reflection.GeneratedProtocolMessageType('TopicConfig', (_message.Message,), {'DESCRIPTOR': _TOPICCONFIG, '__module__': 'modules.planning.planning_base.proto.planning_config_pb2'})
_sym_db.RegisterMessage(TopicConfig)
ReferenceLineConfig = _reflection.GeneratedProtocolMessageType('ReferenceLineConfig', (_message.Message,), {'DESCRIPTOR': _REFERENCELINECONFIG, '__module__': 'modules.planning.planning_base.proto.planning_config_pb2'})
_sym_db.RegisterMessage(ReferenceLineConfig)
PlanningConfig = _reflection.GeneratedProtocolMessageType('PlanningConfig', (_message.Message,), {'DESCRIPTOR': _PLANNINGCONFIG, '__module__': 'modules.planning.planning_base.proto.planning_config_pb2'})
_sym_db.RegisterMessage(PlanningConfig)
if _descriptor._USE_C_DESCRIPTORS == False:
    DESCRIPTOR._options = None
    _TOPICCONFIG._serialized_start = 80
    _TOPICCONFIG._serialized_end = 522
    _REFERENCELINECONFIG._serialized_start = 524
    _REFERENCELINECONFIG._serialized_end = 568
    _PLANNINGCONFIG._serialized_start = 571
    _PLANNINGCONFIG._serialized_end = 908
    _PLANNINGCONFIG_PLANNINGLEARNINGMODE._serialized_start = 804
    _PLANNINGCONFIG_PLANNINGLEARNINGMODE._serialized_end = 908