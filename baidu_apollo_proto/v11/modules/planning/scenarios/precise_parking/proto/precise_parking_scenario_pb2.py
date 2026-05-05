"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
_sym_db = _symbol_database.Default()
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\nOmodules/planning/scenarios/precise_parking/proto/precise_parking_scenario.proto\x12\x0fapollo.planning"\xa8\x02\n\x1cScenarioPreciseParkingConfig\x12$\n\x19precise_trajectory_length\x18\x01 \x01(\x01:\x013\x12)\n\x1benable_perception_obstacles\x18\x02 \x01(\x08:\x04true\x124\n&expand_polygon_of_obstacle_by_distance\x18\x03 \x01(\x08:\x04true\x12\'\n\x1aperception_obstacle_buffer\x18\x04 \x01(\x01:\x030.5\x12\x1e\n\x11max_heading_error\x18\x05 \x01(\x01:\x030.4\x12\x1b\n\rmax_lat_error\x18\x06 \x01(\x01:\x040.12\x12\x1b\n\rmax_lon_error\x18\x07 \x01(\x01:\x040.12')
_SCENARIOPRECISEPARKINGCONFIG = DESCRIPTOR.message_types_by_name['ScenarioPreciseParkingConfig']
ScenarioPreciseParkingConfig = _reflection.GeneratedProtocolMessageType('ScenarioPreciseParkingConfig', (_message.Message,), {'DESCRIPTOR': _SCENARIOPRECISEPARKINGCONFIG, '__module__': 'modules.planning.scenarios.precise_parking.proto.precise_parking_scenario_pb2'})
_sym_db.RegisterMessage(ScenarioPreciseParkingConfig)
if _descriptor._USE_C_DESCRIPTORS == False:
    DESCRIPTOR._options = None
    _SCENARIOPRECISEPARKINGCONFIG._serialized_start = 101
    _SCENARIOPRECISEPARKINGCONFIG._serialized_end = 397