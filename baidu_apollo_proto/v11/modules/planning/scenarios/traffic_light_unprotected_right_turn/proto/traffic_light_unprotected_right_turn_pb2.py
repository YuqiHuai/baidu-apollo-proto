"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
_sym_db = _symbol_database.Default()
from ......modules.planning.planning_interface_base.scenario_base.proto import creep_stage_pb2 as modules_dot_planning_dot_planning__interface__base_dot_scenario__base_dot_proto_dot_creep__stage__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\npmodules/planning/scenarios/traffic_light_unprotected_right_turn/proto/traffic_light_unprotected_right_turn.proto\x12\x0fapollo.planning\x1aNmodules/planning/planning_interface_base/scenario_base/proto/creep_stage.proto"\x89\x03\n.ScenarioTrafficLightUnprotectedRightTurnConfig\x120\n%start_traffic_light_scenario_distance\x18\x01 \x01(\x01:\x015\x12\'\n\x18enable_right_turn_on_red\x18\x02 \x01(\x08:\x05false\x12$\n\x17max_valid_stop_distance\x18\x03 \x01(\x01:\x033.5\x12\x1e\n\x13min_pass_s_distance\x18\x04 \x01(\x01:\x013\x121\n&red_light_right_turn_stop_duration_sec\x18\x05 \x01(\x02:\x013\x12\x1d\n\x11creep_timeout_sec\x18\x06 \x01(\x02:\x0210\x12%\n\x1amax_adc_speed_before_creep\x18\x07 \x01(\x01:\x013\x12=\n\x12creep_stage_config\x18\x08 \x01(\x0b2!.apollo.planning.CreepStageConfig')
_SCENARIOTRAFFICLIGHTUNPROTECTEDRIGHTTURNCONFIG = DESCRIPTOR.message_types_by_name['ScenarioTrafficLightUnprotectedRightTurnConfig']
ScenarioTrafficLightUnprotectedRightTurnConfig = _reflection.GeneratedProtocolMessageType('ScenarioTrafficLightUnprotectedRightTurnConfig', (_message.Message,), {'DESCRIPTOR': _SCENARIOTRAFFICLIGHTUNPROTECTEDRIGHTTURNCONFIG, '__module__': 'modules.planning.scenarios.traffic_light_unprotected_right_turn.proto.traffic_light_unprotected_right_turn_pb2'})
_sym_db.RegisterMessage(ScenarioTrafficLightUnprotectedRightTurnConfig)
if _descriptor._USE_C_DESCRIPTORS == False:
    DESCRIPTOR._options = None
    _SCENARIOTRAFFICLIGHTUNPROTECTEDRIGHTTURNCONFIG._serialized_start = 214
    _SCENARIOTRAFFICLIGHTUNPROTECTEDRIGHTTURNCONFIG._serialized_end = 607