"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
_sym_db = _symbol_database.Default()
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\nQmodules/planning/scenarios/lane_follow_park/proto/lane_follow_park_scenario.proto\x12\x0fapollo.planning"\xf3\x01\n\x1cScenarioLaneFollowParkConfig\x12\x1e\n\x11queue_check_count\x18\x01 \x01(\x05:\x03100\x12\x1e\n\x12stable_block_count\x18\x02 \x01(\x05:\x0230\x12\x1b\n\x0epassby_min_gap\x18\x03 \x01(\x01:\x030.5\x12\x1f\n\x12passby_kappa_ratio\x18\x04 \x01(\x01:\x030.5\x12.\n"min_distance_block_obs_to_junction\x18\x05 \x01(\x01:\x0222\x12%\n\x16enable_junction_borrow\x18\x06 \x01(\x08:\x05false')
_SCENARIOLANEFOLLOWPARKCONFIG = DESCRIPTOR.message_types_by_name['ScenarioLaneFollowParkConfig']
ScenarioLaneFollowParkConfig = _reflection.GeneratedProtocolMessageType('ScenarioLaneFollowParkConfig', (_message.Message,), {'DESCRIPTOR': _SCENARIOLANEFOLLOWPARKCONFIG, '__module__': 'modules.planning.scenarios.lane_follow_park.proto.lane_follow_park_scenario_pb2'})
_sym_db.RegisterMessage(ScenarioLaneFollowParkConfig)
if _descriptor._USE_C_DESCRIPTORS == False:
    DESCRIPTOR._options = None
    _SCENARIOLANEFOLLOWPARKCONFIG._serialized_start = 103
    _SCENARIOLANEFOLLOWPARKCONFIG._serialized_end = 346