"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
_sym_db = _symbol_database.Default()
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\nOmodules/planning/scenarios/large_curvature/proto/large_curvature_scenario.proto\x12\x0fapollo.planning"\xc3\x01\n\x1cScenarioLargeCurvatureConfig\x12\x1a\n\rmin_curvature\x18\x01 \x01(\x01:\x030.2\x12$\n\x17curvature_check_delta_s\x18\x02 \x01(\x01:\x030.3\x12#\n\x18curvature_check_distance\x18\x03 \x01(\x01:\x013\x12 \n\x13curvature_check_max\x18\x04 \x01(\x01:\x030.1\x12\x1a\n\x0fcurvature_ratio\x18\x05 \x01(\x01:\x011')
_SCENARIOLARGECURVATURECONFIG = DESCRIPTOR.message_types_by_name['ScenarioLargeCurvatureConfig']
ScenarioLargeCurvatureConfig = _reflection.GeneratedProtocolMessageType('ScenarioLargeCurvatureConfig', (_message.Message,), {'DESCRIPTOR': _SCENARIOLARGECURVATURECONFIG, '__module__': 'modules.planning.scenarios.large_curvature.proto.large_curvature_scenario_pb2'})
_sym_db.RegisterMessage(ScenarioLargeCurvatureConfig)
if _descriptor._USE_C_DESCRIPTORS == False:
    DESCRIPTOR._options = None
    _SCENARIOLARGECURVATURECONFIG._serialized_start = 101
    _SCENARIOLARGECURVATURECONFIG._serialized_end = 296