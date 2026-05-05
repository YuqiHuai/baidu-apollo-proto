"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
_sym_db = _symbol_database.Default()
from .....modules.common_msgs.basic_msgs import geometry_pb2 as modules_dot_common__msgs_dot_basic__msgs_dot_geometry__pb2
from .....modules.common_msgs.external_command_msgs import lane_follow_command_pb2 as modules_dot_common__msgs_dot_external__command__msgs_dot_lane__follow__command__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n:modules/planning/planning_base/proto/planning_status.proto\x12\x0fapollo.planning\x1a-modules/common_msgs/basic_msgs/geometry.proto\x1aCmodules/common_msgs/external_command_msgs/lane_follow_command.proto"\xc0\x01\n\x10ChangeLaneStatus\x128\n\x06status\x18\x01 \x01(\x0e2(.apollo.planning.ChangeLaneStatus.Status\x12\x0f\n\x07path_id\x18\x02 \x01(\t\x12\x11\n\ttimestamp\x18\x03 \x01(\x01"N\n\x06Status\x12\x12\n\x0eIN_CHANGE_LANE\x10\x01\x12\x16\n\x12CHANGE_LANE_FAILED\x10\x02\x12\x18\n\x14CHANGE_LANE_FINISHED\x10\x03"1\n\x12CreepDeciderStatus\x12\x1b\n\x13creep_clear_counter\x18\x01 \x01(\r";\n\x08StopTime\x12\x13\n\x0bobstacle_id\x18\x01 \x01(\t\x12\x1a\n\x12stop_timestamp_sec\x18\x02 \x01(\x01"q\n\x0fCrosswalkStatus\x12\x14\n\x0ccrosswalk_id\x18\x01 \x01(\t\x12,\n\tstop_time\x18\x02 \x03(\x0b2\x19.apollo.planning.StopTime\x12\x1a\n\x12finished_crosswalk\x18\x03 \x03(\t":\n\x11DestinationStatus\x12%\n\x16has_passed_destination\x18\x01 \x01(\x08:\x05false"H\n\x13EmergencyStopStatus\x121\n\x10stop_fence_point\x18\x01 \x01(\x0b2\x17.apollo.common.PointENU"_\n\x0fOpenSpaceStatus\x12.\n&partitioned_trajectories_index_history\x18\x01 \x03(\t\x12\x1c\n\rposition_init\x18\x02 \x01(\x08:\x05false"\xad\x01\n\x0fParkAndGoStatus\x122\n\x11adc_init_position\x18\x01 \x01(\x0b2\x17.apollo.common.PointENU\x12\x18\n\x10adc_init_heading\x18\x02 \x01(\x01\x12\x16\n\x0ein_check_stage\x18\x03 \x01(\x08\x124\n\x13adc_adjust_end_pose\x18\x04 \x01(\x0b2\x17.apollo.common.PointENU"\xd0\x01\n\x11PathDeciderStatus\x12.\n#front_static_obstacle_cycle_counter\x18\x01 \x01(\x05:\x010\x12.\n\x1fis_in_path_lane_borrow_scenario\x18\x02 \x01(\x08:\x05false\x12"\n\x18front_static_obstacle_id\x18\x03 \x01(\t:\x00\x12\x1a\n\x0bleft_borrow\x18\x04 \x01(\x08:\x05false\x12\x1b\n\x0cright_borrow\x18\x05 \x01(\x08:\x05false"\xc0\x02\n\x0ePullOverStatus\x12D\n\x0epull_over_type\x18\x01 \x01(\x0e2,.apollo.planning.PullOverStatus.PullOverType\x12"\n\x13plan_pull_over_path\x18\x02 \x01(\x08:\x05false\x12)\n\x08position\x18\x03 \x01(\x0b2\x17.apollo.common.PointENU\x12\r\n\x05theta\x18\x04 \x01(\x01\x12\x14\n\x0clength_front\x18\x05 \x01(\x01\x12\x13\n\x0blength_back\x18\x06 \x01(\x01\x12\x12\n\nwidth_left\x18\x07 \x01(\x01\x12\x13\n\x0bwidth_right\x18\x08 \x01(\x01"6\n\x0cPullOverType\x12\r\n\tPULL_OVER\x10\x01\x12\x17\n\x13EMERGENCY_PULL_OVER\x10\x02"\x96\x01\n\x0fReroutingStatus\x12\x1b\n\x13last_rerouting_time\x18\x01 \x01(\x01\x12\x1d\n\x0eneed_rerouting\x18\x02 \x01(\x08:\x05false\x12G\n\x13lane_follow_command\x18\x04 \x01(\x0b2*.apollo.external_command.LaneFollowCommand"M\n\x12SpeedDeciderStatus\x127\n\x14pedestrian_stop_time\x18\x01 \x03(\x0b2\x19.apollo.planning.StopTime";\n\x0eScenarioStatus\x12\x15\n\rscenario_type\x18\x01 \x01(\t\x12\x12\n\nstage_type\x18\x02 \x01(\t"w\n\x0eStopSignStatus\x12$\n\x1ccurrent_stop_sign_overlap_id\x18\x01 \x01(\t\x12!\n\x19done_stop_sign_overlap_id\x18\x02 \x01(\t\x12\x1c\n\x14wait_for_obstacle_id\x18\x03 \x03(\t"e\n\x12TrafficLightStatus\x12(\n current_traffic_light_overlap_id\x18\x01 \x03(\t\x12%\n\x1ddone_traffic_light_overlap_id\x18\x02 \x03(\t"z\n\x0fYieldSignStatus\x12%\n\x1dcurrent_yield_sign_overlap_id\x18\x01 \x03(\t\x12"\n\x1adone_yield_sign_overlap_id\x18\x02 \x03(\t\x12\x1c\n\x14wait_for_obstacle_id\x18\x03 \x03(\t"\x8d\x01\n\x10LaneFollowStatus\x12 \n\x11lane_follow_block\x18\x01 \x01(\x08:\x05false\x12\x1b\n\x11block_obstacle_id\x18\x02 \x01(\t:\x00\x12\x1f\n\x14last_block_timestamp\x18\x03 \x01(\x01:\x010\x12\x19\n\x0eblock_duration\x18\x04 \x01(\x01:\x010"\x8d\x01\n\x10LaneBorrowStatus\x12 \n\x11lane_borrow_block\x18\x01 \x01(\x08:\x05false\x12\x1b\n\x11block_obstacle_id\x18\x02 \x01(\t:\x00\x12\x1f\n\x14last_block_timestamp\x18\x03 \x01(\x01:\x010\x12\x19\n\x0eblock_duration\x18\x04 \x01(\x01:\x010"\xc5\x07\n\x0ePlanningStatus\x126\n\x0bchange_lane\x18\x02 \x01(\x0b2!.apollo.planning.ChangeLaneStatus\x12:\n\rcreep_decider\x18\x03 \x01(\x0b2#.apollo.planning.CreepDeciderStatus\x123\n\tcrosswalk\x18\x04 \x01(\x0b2 .apollo.planning.CrosswalkStatus\x127\n\x0bdestination\x18\x05 \x01(\x0b2".apollo.planning.DestinationStatus\x12<\n\x0eemergency_stop\x18\x06 \x01(\x0b2$.apollo.planning.EmergencyStopStatus\x124\n\nopen_space\x18\x07 \x01(\x0b2 .apollo.planning.OpenSpaceStatus\x125\n\x0bpark_and_go\x18\x08 \x01(\x0b2 .apollo.planning.ParkAndGoStatus\x128\n\x0cpath_decider\x18\t \x01(\x0b2".apollo.planning.PathDeciderStatus\x122\n\tpull_over\x18\n \x01(\x0b2\x1f.apollo.planning.PullOverStatus\x123\n\trerouting\x18\x0b \x01(\x0b2 .apollo.planning.ReroutingStatus\x121\n\x08scenario\x18\x0c \x01(\x0b2\x1f.apollo.planning.ScenarioStatus\x12:\n\rspeed_decider\x18\r \x01(\x0b2#.apollo.planning.SpeedDeciderStatus\x122\n\tstop_sign\x18\x0e \x01(\x0b2\x1f.apollo.planning.StopSignStatus\x12:\n\rtraffic_light\x18\x0f \x01(\x0b2#.apollo.planning.TrafficLightStatus\x124\n\nyield_sign\x18\x10 \x01(\x0b2 .apollo.planning.YieldSignStatus\x126\n\x0blane_follow\x18\x11 \x01(\x0b2!.apollo.planning.LaneFollowStatus\x126\n\x0blane_borrow\x18\x12 \x01(\x0b2!.apollo.planning.LaneBorrowStatus')
_CHANGELANESTATUS = DESCRIPTOR.message_types_by_name['ChangeLaneStatus']
_CREEPDECIDERSTATUS = DESCRIPTOR.message_types_by_name['CreepDeciderStatus']
_STOPTIME = DESCRIPTOR.message_types_by_name['StopTime']
_CROSSWALKSTATUS = DESCRIPTOR.message_types_by_name['CrosswalkStatus']
_DESTINATIONSTATUS = DESCRIPTOR.message_types_by_name['DestinationStatus']
_EMERGENCYSTOPSTATUS = DESCRIPTOR.message_types_by_name['EmergencyStopStatus']
_OPENSPACESTATUS = DESCRIPTOR.message_types_by_name['OpenSpaceStatus']
_PARKANDGOSTATUS = DESCRIPTOR.message_types_by_name['ParkAndGoStatus']
_PATHDECIDERSTATUS = DESCRIPTOR.message_types_by_name['PathDeciderStatus']
_PULLOVERSTATUS = DESCRIPTOR.message_types_by_name['PullOverStatus']
_REROUTINGSTATUS = DESCRIPTOR.message_types_by_name['ReroutingStatus']
_SPEEDDECIDERSTATUS = DESCRIPTOR.message_types_by_name['SpeedDeciderStatus']
_SCENARIOSTATUS = DESCRIPTOR.message_types_by_name['ScenarioStatus']
_STOPSIGNSTATUS = DESCRIPTOR.message_types_by_name['StopSignStatus']
_TRAFFICLIGHTSTATUS = DESCRIPTOR.message_types_by_name['TrafficLightStatus']
_YIELDSIGNSTATUS = DESCRIPTOR.message_types_by_name['YieldSignStatus']
_LANEFOLLOWSTATUS = DESCRIPTOR.message_types_by_name['LaneFollowStatus']
_LANEBORROWSTATUS = DESCRIPTOR.message_types_by_name['LaneBorrowStatus']
_PLANNINGSTATUS = DESCRIPTOR.message_types_by_name['PlanningStatus']
_CHANGELANESTATUS_STATUS = _CHANGELANESTATUS.enum_types_by_name['Status']
_PULLOVERSTATUS_PULLOVERTYPE = _PULLOVERSTATUS.enum_types_by_name['PullOverType']
ChangeLaneStatus = _reflection.GeneratedProtocolMessageType('ChangeLaneStatus', (_message.Message,), {'DESCRIPTOR': _CHANGELANESTATUS, '__module__': 'modules.planning.planning_base.proto.planning_status_pb2'})
_sym_db.RegisterMessage(ChangeLaneStatus)
CreepDeciderStatus = _reflection.GeneratedProtocolMessageType('CreepDeciderStatus', (_message.Message,), {'DESCRIPTOR': _CREEPDECIDERSTATUS, '__module__': 'modules.planning.planning_base.proto.planning_status_pb2'})
_sym_db.RegisterMessage(CreepDeciderStatus)
StopTime = _reflection.GeneratedProtocolMessageType('StopTime', (_message.Message,), {'DESCRIPTOR': _STOPTIME, '__module__': 'modules.planning.planning_base.proto.planning_status_pb2'})
_sym_db.RegisterMessage(StopTime)
CrosswalkStatus = _reflection.GeneratedProtocolMessageType('CrosswalkStatus', (_message.Message,), {'DESCRIPTOR': _CROSSWALKSTATUS, '__module__': 'modules.planning.planning_base.proto.planning_status_pb2'})
_sym_db.RegisterMessage(CrosswalkStatus)
DestinationStatus = _reflection.GeneratedProtocolMessageType('DestinationStatus', (_message.Message,), {'DESCRIPTOR': _DESTINATIONSTATUS, '__module__': 'modules.planning.planning_base.proto.planning_status_pb2'})
_sym_db.RegisterMessage(DestinationStatus)
EmergencyStopStatus = _reflection.GeneratedProtocolMessageType('EmergencyStopStatus', (_message.Message,), {'DESCRIPTOR': _EMERGENCYSTOPSTATUS, '__module__': 'modules.planning.planning_base.proto.planning_status_pb2'})
_sym_db.RegisterMessage(EmergencyStopStatus)
OpenSpaceStatus = _reflection.GeneratedProtocolMessageType('OpenSpaceStatus', (_message.Message,), {'DESCRIPTOR': _OPENSPACESTATUS, '__module__': 'modules.planning.planning_base.proto.planning_status_pb2'})
_sym_db.RegisterMessage(OpenSpaceStatus)
ParkAndGoStatus = _reflection.GeneratedProtocolMessageType('ParkAndGoStatus', (_message.Message,), {'DESCRIPTOR': _PARKANDGOSTATUS, '__module__': 'modules.planning.planning_base.proto.planning_status_pb2'})
_sym_db.RegisterMessage(ParkAndGoStatus)
PathDeciderStatus = _reflection.GeneratedProtocolMessageType('PathDeciderStatus', (_message.Message,), {'DESCRIPTOR': _PATHDECIDERSTATUS, '__module__': 'modules.planning.planning_base.proto.planning_status_pb2'})
_sym_db.RegisterMessage(PathDeciderStatus)
PullOverStatus = _reflection.GeneratedProtocolMessageType('PullOverStatus', (_message.Message,), {'DESCRIPTOR': _PULLOVERSTATUS, '__module__': 'modules.planning.planning_base.proto.planning_status_pb2'})
_sym_db.RegisterMessage(PullOverStatus)
ReroutingStatus = _reflection.GeneratedProtocolMessageType('ReroutingStatus', (_message.Message,), {'DESCRIPTOR': _REROUTINGSTATUS, '__module__': 'modules.planning.planning_base.proto.planning_status_pb2'})
_sym_db.RegisterMessage(ReroutingStatus)
SpeedDeciderStatus = _reflection.GeneratedProtocolMessageType('SpeedDeciderStatus', (_message.Message,), {'DESCRIPTOR': _SPEEDDECIDERSTATUS, '__module__': 'modules.planning.planning_base.proto.planning_status_pb2'})
_sym_db.RegisterMessage(SpeedDeciderStatus)
ScenarioStatus = _reflection.GeneratedProtocolMessageType('ScenarioStatus', (_message.Message,), {'DESCRIPTOR': _SCENARIOSTATUS, '__module__': 'modules.planning.planning_base.proto.planning_status_pb2'})
_sym_db.RegisterMessage(ScenarioStatus)
StopSignStatus = _reflection.GeneratedProtocolMessageType('StopSignStatus', (_message.Message,), {'DESCRIPTOR': _STOPSIGNSTATUS, '__module__': 'modules.planning.planning_base.proto.planning_status_pb2'})
_sym_db.RegisterMessage(StopSignStatus)
TrafficLightStatus = _reflection.GeneratedProtocolMessageType('TrafficLightStatus', (_message.Message,), {'DESCRIPTOR': _TRAFFICLIGHTSTATUS, '__module__': 'modules.planning.planning_base.proto.planning_status_pb2'})
_sym_db.RegisterMessage(TrafficLightStatus)
YieldSignStatus = _reflection.GeneratedProtocolMessageType('YieldSignStatus', (_message.Message,), {'DESCRIPTOR': _YIELDSIGNSTATUS, '__module__': 'modules.planning.planning_base.proto.planning_status_pb2'})
_sym_db.RegisterMessage(YieldSignStatus)
LaneFollowStatus = _reflection.GeneratedProtocolMessageType('LaneFollowStatus', (_message.Message,), {'DESCRIPTOR': _LANEFOLLOWSTATUS, '__module__': 'modules.planning.planning_base.proto.planning_status_pb2'})
_sym_db.RegisterMessage(LaneFollowStatus)
LaneBorrowStatus = _reflection.GeneratedProtocolMessageType('LaneBorrowStatus', (_message.Message,), {'DESCRIPTOR': _LANEBORROWSTATUS, '__module__': 'modules.planning.planning_base.proto.planning_status_pb2'})
_sym_db.RegisterMessage(LaneBorrowStatus)
PlanningStatus = _reflection.GeneratedProtocolMessageType('PlanningStatus', (_message.Message,), {'DESCRIPTOR': _PLANNINGSTATUS, '__module__': 'modules.planning.planning_base.proto.planning_status_pb2'})
_sym_db.RegisterMessage(PlanningStatus)
if _descriptor._USE_C_DESCRIPTORS == False:
    DESCRIPTOR._options = None
    _CHANGELANESTATUS._serialized_start = 196
    _CHANGELANESTATUS._serialized_end = 388
    _CHANGELANESTATUS_STATUS._serialized_start = 310
    _CHANGELANESTATUS_STATUS._serialized_end = 388
    _CREEPDECIDERSTATUS._serialized_start = 390
    _CREEPDECIDERSTATUS._serialized_end = 439
    _STOPTIME._serialized_start = 441
    _STOPTIME._serialized_end = 500
    _CROSSWALKSTATUS._serialized_start = 502
    _CROSSWALKSTATUS._serialized_end = 615
    _DESTINATIONSTATUS._serialized_start = 617
    _DESTINATIONSTATUS._serialized_end = 675
    _EMERGENCYSTOPSTATUS._serialized_start = 677
    _EMERGENCYSTOPSTATUS._serialized_end = 749
    _OPENSPACESTATUS._serialized_start = 751
    _OPENSPACESTATUS._serialized_end = 846
    _PARKANDGOSTATUS._serialized_start = 849
    _PARKANDGOSTATUS._serialized_end = 1022
    _PATHDECIDERSTATUS._serialized_start = 1025
    _PATHDECIDERSTATUS._serialized_end = 1233
    _PULLOVERSTATUS._serialized_start = 1236
    _PULLOVERSTATUS._serialized_end = 1556
    _PULLOVERSTATUS_PULLOVERTYPE._serialized_start = 1502
    _PULLOVERSTATUS_PULLOVERTYPE._serialized_end = 1556
    _REROUTINGSTATUS._serialized_start = 1559
    _REROUTINGSTATUS._serialized_end = 1709
    _SPEEDDECIDERSTATUS._serialized_start = 1711
    _SPEEDDECIDERSTATUS._serialized_end = 1788
    _SCENARIOSTATUS._serialized_start = 1790
    _SCENARIOSTATUS._serialized_end = 1849
    _STOPSIGNSTATUS._serialized_start = 1851
    _STOPSIGNSTATUS._serialized_end = 1970
    _TRAFFICLIGHTSTATUS._serialized_start = 1972
    _TRAFFICLIGHTSTATUS._serialized_end = 2073
    _YIELDSIGNSTATUS._serialized_start = 2075
    _YIELDSIGNSTATUS._serialized_end = 2197
    _LANEFOLLOWSTATUS._serialized_start = 2200
    _LANEFOLLOWSTATUS._serialized_end = 2341
    _LANEBORROWSTATUS._serialized_start = 2344
    _LANEBORROWSTATUS._serialized_end = 2485
    _PLANNINGSTATUS._serialized_start = 2488
    _PLANNINGSTATUS._serialized_end = 3453