"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
_sym_db = _symbol_database.Default()
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\nLmodules/planning/scenarios/valet_parking_park/proto/valet_parking_park.proto\x12\x0fapollo.planning"\xf3\x01\n\x1eScenarioValetParkingParkConfig\x12\'\n\x1bparking_spot_range_to_start\x18\x01 \x01(\x01:\x0220\x12"\n\x17max_valid_stop_distance\x18\x02 \x01(\x01:\x011\x12\x1e\n\x11max_heading_error\x18\x03 \x01(\x01:\x030.1\x12\x1a\n\rmax_lat_error\x18\x04 \x01(\x01:\x030.3\x12\x1a\n\rmax_lon_error\x18\x05 \x01(\x01:\x030.1\x12,\n\x1denable_parallel_retry_parking\x18\x06 \x01(\x08:\x05false')
_SCENARIOVALETPARKINGPARKCONFIG = DESCRIPTOR.message_types_by_name['ScenarioValetParkingParkConfig']
ScenarioValetParkingParkConfig = _reflection.GeneratedProtocolMessageType('ScenarioValetParkingParkConfig', (_message.Message,), {'DESCRIPTOR': _SCENARIOVALETPARKINGPARKCONFIG, '__module__': 'modules.planning.scenarios.valet_parking_park.proto.valet_parking_park_pb2'})
_sym_db.RegisterMessage(ScenarioValetParkingParkConfig)
if _descriptor._USE_C_DESCRIPTORS == False:
    DESCRIPTOR._options = None
    _SCENARIOVALETPARKINGPARKCONFIG._serialized_start = 98
    _SCENARIOVALETPARKINGPARKCONFIG._serialized_end = 341