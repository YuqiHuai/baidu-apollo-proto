"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
_sym_db = _symbol_database.Default()
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\nEmodules/planning/scenarios/free_space/proto/free_space_scenario.proto\x12\x0fapollo.planning"\x8b\x01\n\x17ScenarioFreeSpaceConfig\x12*\n\x1cenabled_perception_obstacles\x18\x01 \x01(\x08:\x04true\x12 \n\x12filtering_distance\x18\x02 \x01(\x01:\x041000\x12"\n\x1aperception_obstacle_buffer\x18\x03 \x01(\x01')
_SCENARIOFREESPACECONFIG = DESCRIPTOR.message_types_by_name['ScenarioFreeSpaceConfig']
ScenarioFreeSpaceConfig = _reflection.GeneratedProtocolMessageType('ScenarioFreeSpaceConfig', (_message.Message,), {'DESCRIPTOR': _SCENARIOFREESPACECONFIG, '__module__': 'modules.planning.scenarios.free_space.proto.free_space_scenario_pb2'})
_sym_db.RegisterMessage(ScenarioFreeSpaceConfig)
if _descriptor._USE_C_DESCRIPTORS == False:
    DESCRIPTOR._options = None
    _SCENARIOFREESPACECONFIG._serialized_start = 91
    _SCENARIOFREESPACECONFIG._serialized_end = 230