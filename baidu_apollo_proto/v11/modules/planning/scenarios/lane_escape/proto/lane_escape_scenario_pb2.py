"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
_sym_db = _symbol_database.Default()
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\nGmodules/planning/scenarios/lane_escape/proto/lane_escape_scenario.proto\x12\x0fapollo.planning"\xbf\x01\n\x18ScenarioLaneEscapeConfig\x12"\n\x17escape_reverse_distance\x18\x01 \x01(\x01:\x015\x12\x1f\n\x14escape_stop_distance\x18\x02 \x01(\x01:\x011\x12\x1e\n\x12success_path_count\x18\x03 \x01(\x05:\x0210\x12\x1d\n\x11stop_check_window\x18\x06 \x01(\x05:\x0210\x12\x1f\n\x13forward_path_length\x18\x07 \x01(\x01:\x0215')
_SCENARIOLANEESCAPECONFIG = DESCRIPTOR.message_types_by_name['ScenarioLaneEscapeConfig']
ScenarioLaneEscapeConfig = _reflection.GeneratedProtocolMessageType('ScenarioLaneEscapeConfig', (_message.Message,), {'DESCRIPTOR': _SCENARIOLANEESCAPECONFIG, '__module__': 'modules.planning.scenarios.lane_escape.proto.lane_escape_scenario_pb2'})
_sym_db.RegisterMessage(ScenarioLaneEscapeConfig)
if _descriptor._USE_C_DESCRIPTORS == False:
    DESCRIPTOR._options = None
    _SCENARIOLANEESCAPECONFIG._serialized_start = 93
    _SCENARIOLANEESCAPECONFIG._serialized_end = 284