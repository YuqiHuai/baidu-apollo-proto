"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
_sym_db = _symbol_database.Default()
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\nBmodules/planning/scenarios/valet_parking/proto/valet_parking.proto\x12\x0fapollo.planning"i\n\x1aScenarioValetParkingConfig\x12\'\n\x1bparking_spot_range_to_start\x18\x01 \x01(\x01:\x0220\x12"\n\x17max_valid_stop_distance\x18\x02 \x01(\x01:\x011')
_SCENARIOVALETPARKINGCONFIG = DESCRIPTOR.message_types_by_name['ScenarioValetParkingConfig']
ScenarioValetParkingConfig = _reflection.GeneratedProtocolMessageType('ScenarioValetParkingConfig', (_message.Message,), {'DESCRIPTOR': _SCENARIOVALETPARKINGCONFIG, '__module__': 'modules.planning.scenarios.valet_parking.proto.valet_parking_pb2'})
_sym_db.RegisterMessage(ScenarioValetParkingConfig)
if _descriptor._USE_C_DESCRIPTORS == False:
    DESCRIPTOR._options = None
    _SCENARIOVALETPARKINGCONFIG._serialized_start = 87
    _SCENARIOVALETPARKINGCONFIG._serialized_end = 192