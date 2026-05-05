"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
_sym_db = _symbol_database.Default()
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n4modules/planning/scenarios/square/proto/square.proto\x12\x0fapollo.planning"^\n\x14ScenarioSquareConfig\x12\x1f\n\x12filtering_distance\x18\x01 \x01(\x01:\x03100\x12%\n\x1aperception_obstacle_buffer\x18\x02 \x01(\x01:\x012')
_SCENARIOSQUARECONFIG = DESCRIPTOR.message_types_by_name['ScenarioSquareConfig']
ScenarioSquareConfig = _reflection.GeneratedProtocolMessageType('ScenarioSquareConfig', (_message.Message,), {'DESCRIPTOR': _SCENARIOSQUARECONFIG, '__module__': 'modules.planning.scenarios.square.proto.square_pb2'})
_sym_db.RegisterMessage(ScenarioSquareConfig)
if _descriptor._USE_C_DESCRIPTORS == False:
    DESCRIPTOR._options = None
    _SCENARIOSQUARECONFIG._serialized_start = 73
    _SCENARIOSQUARECONFIG._serialized_end = 167