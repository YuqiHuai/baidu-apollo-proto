"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
_sym_db = _symbol_database.Default()
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n/modules/common_msgs/simulation_msgs/agent.proto\x12\x11apollo.simulation"\xbc\n\n\x0bAgentConfig\x12\n\n\x02id\x18\x01 \x01(\x05\x12\x13\n\x0bdescription\x18\x02 \x01(\t\x12\x10\n\x05width\x18\x03 \x01(\x01:\x012\x12\x11\n\x06length\x18\x04 \x01(\x01:\x015\x12\x13\n\x06height\x18\x05 \x01(\x01:\x031.8\x121\n\x04type\x18\x06 \x01(\x0e2#.apollo.simulation.AgentConfig.Type\x12\x17\n\x0bappear_time\x18\x07 \x01(\x01B\x02\x18\x01\x12\x1a\n\x0edisappear_time\x18\x08 \x01(\x01B\x02\x18\x01\x12B\n\rtracked_point\x18\t \x03(\x0b2+.apollo.simulation.AgentConfig.TrackedPoint\x12=\n\nmotiontype\x18\n \x01(\x0e2).apollo.simulation.AgentConfig.MotionType\x12\x10\n\x08distance\x18\x0b \x01(\x01\x12C\n\x0estart_position\x18\x0c \x01(\x0b2+.apollo.simulation.AgentConfig.TrackedPoint\x12A\n\x0cend_position\x18\x0e \x01(\x0b2+.apollo.simulation.AgentConfig.TrackedPoint\x12\x12\n\nstart_lane\x18\x0f \x01(\t\x12\x10\n\x08end_lane\x18\x10 \x01(\t\x12@\n\x0ctrigger_type\x18\x14 \x01(\x0e2*.apollo.simulation.AgentConfig.TriggerType\x12\x16\n\x0estart_distance\x18\r \x01(\x01\x12\x15\n\nstart_time\x18\x15 \x01(\x01:\x010\x12&\n\x18avoid_rear_end_collision\x18\x11 \x01(\x08:\x04true\x12*\n\x1brear_end_collision_distance\x18\x12 \x01(\x01:\x013B\x02\x18\x01\x128\n\x08near_car\x18\x13 \x01(\x0b2&.apollo.simulation.AgentConfig.NearCar\x12D\n\x0enear_crosswalk\x18\x16 \x01(\x0b2,.apollo.simulation.AgentConfig.NearCrosswalk\x1aZ\n\x0cTrackedPoint\x12\t\n\x01x\x18\x01 \x01(\x01\x12\t\n\x01y\x18\x02 \x01(\x01\x12\x0f\n\x07heading\x18\x03 \x01(\x01\x12\r\n\x05speed\x18\x04 \x01(\x01\x12\x14\n\x0cacceleration\x18\x05 \x01(\x01\x1ay\n\x07NearCar\x12\x14\n\x08distance\x18\x01 \x01(\x01:\x0220\x12\x18\n\x0cacceleration\x18\x02 \x01(\x01:\x02-2\x12\x1b\n\x0cis_same_lane\x18\x03 \x01(\x08:\x05false\x12!\n\x13only_include_behind\x18\x04 \x01(\x08:\x04true\x1a?\n\rNearCrosswalk\x12\x14\n\x08distance\x18\x01 \x01(\x01:\x0215\x12\x18\n\x0cacceleration\x18\x02 \x01(\x01:\x02-1"k\n\x04Type\x12\x0b\n\x07VEHICLE\x10\x00\x12\x0b\n\x07BICYCLE\x10\x01\x12\x0e\n\nPEDESTRIAN\x10\x02\x12\x15\n\x11UNKNOWN_UNMOVABLE\x10\x03\x12\x13\n\x0fUNKNOWN_MOVABLE\x10\x04\x12\r\n\tBIG_TRUCK\x10\x05"6\n\nMotionType\x12\n\n\x06STATIC\x10\x00\x12\x0f\n\x0bLANE_FOLLOW\x10\x01\x12\x0b\n\x07TRACKED\x10\x02"%\n\x0bTriggerType\x12\x0c\n\x08DISTANCE\x10\x00\x12\x08\n\x04TIME\x10\x01')
_AGENTCONFIG = DESCRIPTOR.message_types_by_name['AgentConfig']
_AGENTCONFIG_TRACKEDPOINT = _AGENTCONFIG.nested_types_by_name['TrackedPoint']
_AGENTCONFIG_NEARCAR = _AGENTCONFIG.nested_types_by_name['NearCar']
_AGENTCONFIG_NEARCROSSWALK = _AGENTCONFIG.nested_types_by_name['NearCrosswalk']
_AGENTCONFIG_TYPE = _AGENTCONFIG.enum_types_by_name['Type']
_AGENTCONFIG_MOTIONTYPE = _AGENTCONFIG.enum_types_by_name['MotionType']
_AGENTCONFIG_TRIGGERTYPE = _AGENTCONFIG.enum_types_by_name['TriggerType']
AgentConfig = _reflection.GeneratedProtocolMessageType('AgentConfig', (_message.Message,), {'TrackedPoint': _reflection.GeneratedProtocolMessageType('TrackedPoint', (_message.Message,), {'DESCRIPTOR': _AGENTCONFIG_TRACKEDPOINT, '__module__': 'modules.common_msgs.simulation_msgs.agent_pb2'}), 'NearCar': _reflection.GeneratedProtocolMessageType('NearCar', (_message.Message,), {'DESCRIPTOR': _AGENTCONFIG_NEARCAR, '__module__': 'modules.common_msgs.simulation_msgs.agent_pb2'}), 'NearCrosswalk': _reflection.GeneratedProtocolMessageType('NearCrosswalk', (_message.Message,), {'DESCRIPTOR': _AGENTCONFIG_NEARCROSSWALK, '__module__': 'modules.common_msgs.simulation_msgs.agent_pb2'}), 'DESCRIPTOR': _AGENTCONFIG, '__module__': 'modules.common_msgs.simulation_msgs.agent_pb2'})
_sym_db.RegisterMessage(AgentConfig)
_sym_db.RegisterMessage(AgentConfig.TrackedPoint)
_sym_db.RegisterMessage(AgentConfig.NearCar)
_sym_db.RegisterMessage(AgentConfig.NearCrosswalk)
if _descriptor._USE_C_DESCRIPTORS == False:
    DESCRIPTOR._options = None
    _AGENTCONFIG.fields_by_name['appear_time']._options = None
    _AGENTCONFIG.fields_by_name['appear_time']._serialized_options = b'\x18\x01'
    _AGENTCONFIG.fields_by_name['disappear_time']._options = None
    _AGENTCONFIG.fields_by_name['disappear_time']._serialized_options = b'\x18\x01'
    _AGENTCONFIG.fields_by_name['rear_end_collision_distance']._options = None
    _AGENTCONFIG.fields_by_name['rear_end_collision_distance']._serialized_options = b'\x18\x01'
    _AGENTCONFIG._serialized_start = 71
    _AGENTCONFIG._serialized_end = 1411
    _AGENTCONFIG_TRACKEDPOINT._serialized_start = 929
    _AGENTCONFIG_TRACKEDPOINT._serialized_end = 1019
    _AGENTCONFIG_NEARCAR._serialized_start = 1021
    _AGENTCONFIG_NEARCAR._serialized_end = 1142
    _AGENTCONFIG_NEARCROSSWALK._serialized_start = 1144
    _AGENTCONFIG_NEARCROSSWALK._serialized_end = 1207
    _AGENTCONFIG_TYPE._serialized_start = 1209
    _AGENTCONFIG_TYPE._serialized_end = 1316
    _AGENTCONFIG_MOTIONTYPE._serialized_start = 1318
    _AGENTCONFIG_MOTIONTYPE._serialized_end = 1372
    _AGENTCONFIG_TRIGGERTYPE._serialized_start = 1374
    _AGENTCONFIG_TRIGGERTYPE._serialized_end = 1411