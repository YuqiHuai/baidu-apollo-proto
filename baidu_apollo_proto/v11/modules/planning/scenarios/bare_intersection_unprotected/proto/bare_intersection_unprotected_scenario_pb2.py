"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
_sym_db = _symbol_database.Default()
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\nkmodules/planning/scenarios/bare_intersection_unprotected/proto/bare_intersection_unprotected_scenario.proto\x12\x0fapollo.planning"\xca\x01\n)ScenarioBareIntersectionUnprotectedConfig\x125\n)start_bare_intersection_scenario_distance\x18\x01 \x01(\x01:\x0225\x12#\n\x14enable_explicit_stop\x18\x02 \x01(\x08:\x05false\x12%\n\x15approach_cruise_speed\x18\x03 \x01(\x01:\x066.7056\x12\x1a\n\rstop_distance\x18\x04 \x01(\x01:\x030.5')
_SCENARIOBAREINTERSECTIONUNPROTECTEDCONFIG = DESCRIPTOR.message_types_by_name['ScenarioBareIntersectionUnprotectedConfig']
ScenarioBareIntersectionUnprotectedConfig = _reflection.GeneratedProtocolMessageType('ScenarioBareIntersectionUnprotectedConfig', (_message.Message,), {'DESCRIPTOR': _SCENARIOBAREINTERSECTIONUNPROTECTEDCONFIG, '__module__': 'modules.planning.scenarios.bare_intersection_unprotected.proto.bare_intersection_unprotected_scenario_pb2'})
_sym_db.RegisterMessage(ScenarioBareIntersectionUnprotectedConfig)
if _descriptor._USE_C_DESCRIPTORS == False:
    DESCRIPTOR._options = None
    _SCENARIOBAREINTERSECTIONUNPROTECTEDCONFIG._serialized_start = 129
    _SCENARIOBAREINTERSECTIONUNPROTECTEDCONFIG._serialized_end = 331