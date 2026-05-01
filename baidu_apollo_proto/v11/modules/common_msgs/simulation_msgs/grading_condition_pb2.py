"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
_sym_db = _symbol_database.Default()
from ....modules.common_msgs.map_msgs import map_geometry_pb2 as modules_dot_common__msgs_dot_map__msgs_dot_map__geometry__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n;modules/common_msgs/simulation_msgs/grading_condition.proto\x12\x11apollo.simulation\x1a/modules/common_msgs/map_msgs/map_geometry.proto"\xd6\x12\n\tCondition\x12@\n\x11logical_condition\x18\x01 \x01(\x0b2#.apollo.simulation.LogicalConditionH\x00\x12<\n\x0fspeed_condition\x18\x02 \x01(\x0b2!.apollo.simulation.SpeedConditionH\x00\x12J\n\x16acceleration_condition\x18\x03 \x01(\x0b2(.apollo.simulation.AccelerationConditionH\x00\x12:\n\x0ejerk_condition\x18\x04 \x01(\x0b2 .apollo.simulation.JerkConditionH\x00\x12M\n\x18object_overlap_condition\x18\x05 \x01(\x0b2).apollo.simulation.ObjectOverlapConditionH\x00\x12M\n\x18region_overlap_condition\x18\x06 \x01(\x0b2).apollo.simulation.RegionOverlapConditionH\x00\x12R\n\x1bregion_overlap_lw_condition\x18\x07 \x01(\x0b2+.apollo.simulation.RegionOverlapLWConditionH\x00\x12:\n\x0espin_condition\x18\x08 \x01(\x0b2 .apollo.simulation.SpinConditionH\x00\x12?\n\x11on_road_condition\x18\t \x01(\x0b2".apollo.simulation.OnRoadConditionH\x00\x12J\n\x17run_red_light_condition\x18\n \x01(\x0b2\'.apollo.simulation.RunRedLightConditionH\x00\x12]\n!change_lane_at_junction_condition\x18\x0b \x01(\x0b20.apollo.simulation.ChangeLaneAtJunctionConditionH\x00\x12@\n\x11routing_condition\x18\x0c \x01(\x0b2#.apollo.simulation.RoutingConditionH\x00\x12O\n\x19crosswalk_yield_condition\x18\r \x01(\x0b2*.apollo.simulation.CrosswalkYieldConditionH\x00\x12K\n\x17abnormal_stop_condition\x18\x0e \x01(\x0b2(.apollo.simulation.AbnormalStopConditionH\x00\x12C\n\x13brake_tap_condition\x18\x0f \x01(\x0b2$.apollo.simulation.BrakeTapConditionH\x00\x12J\n\x17run_stop_sign_condition\x18\x10 \x01(\x0b2\'.apollo.simulation.RunStopSignConditionH\x00\x12F\n\x14checkpoint_condition\x18\x11 \x01(\x0b2&.apollo.simulation.CheckpointConditionH\x00\x12F\n\x15dist_to_end_condition\x18\x12 \x01(\x0b2%.apollo.simulation.DistToEndConditionH\x00\x12U\n\x1ddist_to_lane_center_condition\x18\x13 \x01(\x0b2,.apollo.simulation.DistToLaneCenterConditionH\x00\x12M\n\x18crosswalk_stop_condition\x18\x14 \x01(\x0b2).apollo.simulation.CrosswalkStopConditionH\x00\x12L\n\x18red_light_stop_condition\x18\x15 \x01(\x0b2(.apollo.simulation.RedLightStopConditionH\x00\x12O\n\x19speedbump_limit_condition\x18\x16 \x01(\x0b2*.apollo.simulation.SpeedbumpLimitConditionH\x00\x12_\n"working_zone_avoid_limit_condition\x18\x17 \x01(\x0b21.apollo.simulation.WorkingZoneAvoidLimitConditionH\x00\x12X\n\x1elimited_time_parking_condition\x18\x18 \x01(\x0b2..apollo.simulation.LimitedTimeParkingConditionH\x00\x12R\n\x1bfollow_and_bypass_condition\x18\x19 \x01(\x0b2+.apollo.simulation.FollowAndBypassConditionH\x00\x12O\n\x19obstacle_bypass_condition\x18\x1a \x01(\x0b2*.apollo.simulation.ObstacleBypassConditionH\x00\x12a\n"centripetal_acceleration_condition\x18\x1b \x01(\x0b23.apollo.simulation.CentripetalAccelerationConditionH\x00\x12E\n\x14time_limit_condition\x18\x1c \x01(\x0b2%.apollo.simulation.TimeLimitConditionH\x00\x12K\n\x17anti_cheating_condition\x18\x1d \x01(\x0b2(.apollo.simulation.AntiCheatingConditionH\x00\x12C\n\x13key_point_condition\x18\x1e \x01(\x0b2$.apollo.simulation.KeyPointConditionH\x00\x128\n\x0egrade_planning\x18d \x01(\x0b2 .apollo.simulation.GradePlanningB\x0b\n\tcondition"m\n\rGradePlanning\x12\x13\n\x08duration\x18\x01 \x01(\x11:\x010\x12\x1f\n\x10update_obstacles\x18\x02 \x01(\x08:\x05false\x12&\n\x17use_planning_as_history\x18\x03 \x01(\x08:\x05false"\xdb\x01\n\x10LogicalCondition\x12G\n\roperator_type\x18\x01 \x01(\x0e20.apollo.simulation.LogicalCondition.OperatorType\x123\n\rsub_condition\x18\x02 \x03(\x0b2\x1c.apollo.simulation.Condition"I\n\x0cOperatorType\x12\x0b\n\x07UNKNOWN\x10\x00\x12\x07\n\x03NOT\x10\x01\x12\x07\n\x03AND\x10\x02\x12\x06\n\x02OR\x10\x03\x12\t\n\x05IMPLY\x10\x04\x12\x07\n\x03XOR\x10\x05"\x90\x01\n\x0eSpeedCondition\x12\x13\n\x04name\x18\x01 \x01(\t:\x05speed\x12\x17\n\tmin_speed\x18\x02 \x01(\x01:\x04-0.5\x12\x17\n\tmax_speed\x18\x03 \x01(\x01:\x041000\x12\x18\n\tuse_score\x18\x04 \x01(\x08:\x05false\x12\x1d\n\x10single_deduction\x18\x05 \x01(\x01:\x030.5"\xac\x01\n CentripetalAccelerationCondition\x12&\n\x04name\x18\x01 \x01(\t:\x18centripetal_acceleration\x12\'\n\x1cmax_centripetal_acceleration\x18\x02 \x01(\x01:\x012\x12\x18\n\tuse_score\x18\x03 \x01(\x08:\x05false\x12\x1d\n\x10single_deduction\x18\x04 \x01(\x01:\x030.5"\xad\x01\n\x15AccelerationCondition\x12\x1a\n\x04name\x18\x01 \x01(\t:\x0cacceleration\x12\x1f\n\x10min_acceleration\x18\x02 \x01(\x01:\x05-1000\x12\x1e\n\x10max_acceleration\x18\x03 \x01(\x01:\x041000\x12\x18\n\tuse_score\x18\x04 \x01(\x08:\x05false\x12\x1d\n\x10single_deduction\x18\x05 \x01(\x01:\x030.5"T\n\rJerkCondition\x12\x12\n\x04name\x18\x01 \x01(\t:\x04jerk\x12\x17\n\x08min_jerk\x18\x02 \x01(\x01:\x05-1000\x12\x16\n\x08max_jerk\x18\x03 \x01(\x01:\x041000"T\n\rSpinCondition\x12\x12\n\x04name\x18\x01 \x01(\t:\x04spin\x12\x17\n\x08min_spin\x18\x02 \x01(\x01:\x05-1000\x12\x16\n\x08max_spin\x18\x03 \x01(\x01:\x041000"\xa4\x02\n\x16ObjectOverlapCondition\x12\x19\n\x11source_object_ids\x18\x01 \x01(\t\x12\x19\n\x11target_object_ids\x18\x02 \x01(\t\x12\x10\n\x08distance\x18\x03 \x01(\x01\x12X\n\tdirection\x18\x04 \x01(\x0e27.apollo.simulation.ObjectOverlapCondition.DirectionType:\x0cEXCLUDE_BACK\x12\x19\n\x11ignore_object_ids\x18\x05 \x03(\t\x12\x18\n\tuse_score\x18\x06 \x01(\x08:\x05false"3\n\rDirectionType\x12\x10\n\x0cEXCLUDE_BACK\x10\x00\x12\x10\n\x0cINCLUDE_BACK\x10\x01"\x94\x01\n\x16RegionOverlapCondition\x12\x12\n\nobject_ids\x18\x01 \x01(\t\x12\x1c\n\x10region_corner_xy\x18\x02 \x03(\x01B\x02\x10\x01\x12\x1d\n\x15require_fully_contain\x18\x03 \x01(\x08\x12\x0f\n\x07heading\x18\x04 \x01(\x01\x12\x18\n\tuse_score\x18\x05 \x01(\x08:\x05false"\x9c\x01\n\x18RegionOverlapLWCondition\x12\x12\n\nobject_ids\x18\x01 \x01(\t\x12\t\n\x01x\x18\x02 \x01(\x01\x12\t\n\x01y\x18\x03 \x01(\x01\x12\x0e\n\x06length\x18\x04 \x01(\x01\x12\r\n\x05width\x18\x05 \x01(\x01\x12\x1d\n\x15require_fully_contain\x18\x06 \x01(\x08\x12\x18\n\tuse_score\x18\x07 \x01(\x08:\x05false"M\n\x0fOnRoadCondition\x12 \n\x11use_road_boundary\x18\x01 \x01(\x08:\x05false\x12\x18\n\tuse_score\x18\x02 \x01(\x08:\x05false"0\n\x14RunRedLightCondition\x12\x18\n\tuse_score\x18\x01 \x01(\x08:\x05false"\x82\x01\n\x15RedLightStopCondition\x12\x17\n\x0cmin_distance\x18\x01 \x01(\x01:\x012\x12\x19\n\x0cmax_distance\x18\x02 \x01(\x01:\x032.2\x12\x18\n\tuse_score\x18\x03 \x01(\x08:\x05false\x12\x1b\n\x10single_deduction\x18\x04 \x01(\x01:\x015"\x1f\n\x1dChangeLaneAtJunctionCondition"\x12\n\x10RoutingCondition"\x19\n\x17CrosswalkYieldCondition"\x85\x01\n\x16CrosswalkStopCondition\x12\x19\n\x0cmin_distance\x18\x01 \x01(\x01:\x032.2\x12\x19\n\x0cmax_distance\x18\x02 \x01(\x01:\x032.7\x12\x18\n\tuse_score\x18\x03 \x01(\x08:\x05false\x12\x1b\n\x10single_deduction\x18\x04 \x01(\x01:\x015"X\n\x15AbnormalStopCondition\x12\x13\n\x08duration\x18\x01 \x01(\x01:\x015\x12\x14\n\x08distance\x18\x02 \x01(\x01:\x0210\x12\t\n\x01x\x18\x03 \x01(\x01\x12\t\n\x01y\x18\x04 \x01(\x01"E\n\x11BrakeTapCondition\x12\x17\n\x0cmin_duration\x18\x01 \x01(\x01:\x011\x12\x17\n\x0cmax_duration\x18\x02 \x01(\x01:\x014"+\n\x14RunStopSignCondition\x12\x13\n\x08distance\x18\x01 \x01(\x01:\x012"G\n\x13CheckpointCondition\x120\n\ncheckpoint\x18\x01 \x03(\x0b2\x1c.apollo.simulation.Condition"\x14\n\x12DistToEndCondition"\x1b\n\x19DistToLaneCenterCondition"?\n\x12TimeLimitCondition\x12\x0f\n\x07timeout\x18\x01 \x01(\x01\x12\x18\n\tuse_score\x18\x02 \x01(\x08:\x05false"\xaa\x01\n\x17SpeedbumpLimitCondition\x12!\n\x14speedbump_half_width\x18\x01 \x01(\x01:\x030.2\x12\x14\n\tmax_speed\x18\x02 \x01(\x01:\x013\x12\x1f\n\x14deduction_speed_unit\x18\x03 \x01(\x01:\x011\x12\x18\n\tuse_score\x18\x04 \x01(\x08:\x05false\x12\x1b\n\x10single_deduction\x18\x05 \x01(\x01:\x015"\xc8\x01\n\x1eWorkingZoneAvoidLimitCondition\x12+\n\x0cworking_zone\x18\x01 \x03(\x0b2\x15.apollo.hdmap.Polygon\x12\x17\n\tmax_speed\x18\x02 \x01(\x01:\x048.33\x12)\n\nwhole_area\x18\x03 \x01(\x0b2\x15.apollo.hdmap.Polygon\x12\x18\n\tuse_score\x18\x04 \x01(\x08:\x05false\x12\x1b\n\x10single_deduction\x18\x05 \x01(\x01:\x013"\x80\x01\n\x1bLimitedTimeParkingCondition\x12*\n\x0bparking_lot\x18\x01 \x01(\x0b2\x15.apollo.hdmap.Polygon\x12\x18\n\tuse_score\x18\x02 \x01(\x08:\x05false\x12\x1b\n\x10single_deduction\x18\x03 \x01(\x01:\x015"\xba\x01\n\x18FollowAndBypassCondition\x12)\n\ntest_range\x18\x01 \x01(\x0b2\x15.apollo.hdmap.Polygon\x12\x17\n\x0cdivide_speed\x18\x02 \x01(\x01:\x013\x12\x13\n\x0bobstacle_id\x18\x03 \x01(\t\x12+\n\x08end_line\x18\x04 \x01(\x0b2\x19.apollo.hdmap.LineSegment\x12\x18\n\tuse_score\x18\x05 \x01(\x08:\x05false"\xc7\x01\n\x17ObstacleBypassCondition\x12)\n\ntest_range\x18\x01 \x01(\x0b2\x15.apollo.hdmap.Polygon\x12\x13\n\x0bobstacle_id\x18\x02 \x01(\t\x12\x1f\n\x14min_lateral_distance\x18\x03 \x01(\x01:\x011\x12\x14\n\tmax_speed\x18\x04 \x01(\x01:\x015\x12\x18\n\tuse_score\x18\x05 \x01(\x08:\x05false\x12\x1b\n\x10single_deduction\x18\x06 \x01(\x01:\x015"1\n\x15AntiCheatingCondition\x12\x18\n\tuse_score\x18\x01 \x01(\x08:\x05false"A\n\x08KeyPoint\x12\t\n\x01x\x18\x01 \x01(\x01\x12\t\n\x01y\x18\x02 \x01(\x01\x12\x0c\n\x01z\x18\x03 \x01(\x01:\x010\x12\x11\n\x06radius\x18\x04 \x01(\x01:\x012"\x84\x01\n\x11KeyPointCondition\x12\x18\n\tuse_score\x18\x01 \x01(\x08:\x05false\x12\x16\n\x08in_order\x18\x02 \x01(\x08:\x04true\x12\x11\n\x06radius\x18\x03 \x01(\x01:\x012\x12*\n\x05point\x18\x04 \x03(\x0b2\x1b.apollo.simulation.KeyPoint')
_CONDITION = DESCRIPTOR.message_types_by_name['Condition']
_GRADEPLANNING = DESCRIPTOR.message_types_by_name['GradePlanning']
_LOGICALCONDITION = DESCRIPTOR.message_types_by_name['LogicalCondition']
_SPEEDCONDITION = DESCRIPTOR.message_types_by_name['SpeedCondition']
_CENTRIPETALACCELERATIONCONDITION = DESCRIPTOR.message_types_by_name['CentripetalAccelerationCondition']
_ACCELERATIONCONDITION = DESCRIPTOR.message_types_by_name['AccelerationCondition']
_JERKCONDITION = DESCRIPTOR.message_types_by_name['JerkCondition']
_SPINCONDITION = DESCRIPTOR.message_types_by_name['SpinCondition']
_OBJECTOVERLAPCONDITION = DESCRIPTOR.message_types_by_name['ObjectOverlapCondition']
_REGIONOVERLAPCONDITION = DESCRIPTOR.message_types_by_name['RegionOverlapCondition']
_REGIONOVERLAPLWCONDITION = DESCRIPTOR.message_types_by_name['RegionOverlapLWCondition']
_ONROADCONDITION = DESCRIPTOR.message_types_by_name['OnRoadCondition']
_RUNREDLIGHTCONDITION = DESCRIPTOR.message_types_by_name['RunRedLightCondition']
_REDLIGHTSTOPCONDITION = DESCRIPTOR.message_types_by_name['RedLightStopCondition']
_CHANGELANEATJUNCTIONCONDITION = DESCRIPTOR.message_types_by_name['ChangeLaneAtJunctionCondition']
_ROUTINGCONDITION = DESCRIPTOR.message_types_by_name['RoutingCondition']
_CROSSWALKYIELDCONDITION = DESCRIPTOR.message_types_by_name['CrosswalkYieldCondition']
_CROSSWALKSTOPCONDITION = DESCRIPTOR.message_types_by_name['CrosswalkStopCondition']
_ABNORMALSTOPCONDITION = DESCRIPTOR.message_types_by_name['AbnormalStopCondition']
_BRAKETAPCONDITION = DESCRIPTOR.message_types_by_name['BrakeTapCondition']
_RUNSTOPSIGNCONDITION = DESCRIPTOR.message_types_by_name['RunStopSignCondition']
_CHECKPOINTCONDITION = DESCRIPTOR.message_types_by_name['CheckpointCondition']
_DISTTOENDCONDITION = DESCRIPTOR.message_types_by_name['DistToEndCondition']
_DISTTOLANECENTERCONDITION = DESCRIPTOR.message_types_by_name['DistToLaneCenterCondition']
_TIMELIMITCONDITION = DESCRIPTOR.message_types_by_name['TimeLimitCondition']
_SPEEDBUMPLIMITCONDITION = DESCRIPTOR.message_types_by_name['SpeedbumpLimitCondition']
_WORKINGZONEAVOIDLIMITCONDITION = DESCRIPTOR.message_types_by_name['WorkingZoneAvoidLimitCondition']
_LIMITEDTIMEPARKINGCONDITION = DESCRIPTOR.message_types_by_name['LimitedTimeParkingCondition']
_FOLLOWANDBYPASSCONDITION = DESCRIPTOR.message_types_by_name['FollowAndBypassCondition']
_OBSTACLEBYPASSCONDITION = DESCRIPTOR.message_types_by_name['ObstacleBypassCondition']
_ANTICHEATINGCONDITION = DESCRIPTOR.message_types_by_name['AntiCheatingCondition']
_KEYPOINT = DESCRIPTOR.message_types_by_name['KeyPoint']
_KEYPOINTCONDITION = DESCRIPTOR.message_types_by_name['KeyPointCondition']
_LOGICALCONDITION_OPERATORTYPE = _LOGICALCONDITION.enum_types_by_name['OperatorType']
_OBJECTOVERLAPCONDITION_DIRECTIONTYPE = _OBJECTOVERLAPCONDITION.enum_types_by_name['DirectionType']
Condition = _reflection.GeneratedProtocolMessageType('Condition', (_message.Message,), {'DESCRIPTOR': _CONDITION, '__module__': 'modules.common_msgs.simulation_msgs.grading_condition_pb2'})
_sym_db.RegisterMessage(Condition)
GradePlanning = _reflection.GeneratedProtocolMessageType('GradePlanning', (_message.Message,), {'DESCRIPTOR': _GRADEPLANNING, '__module__': 'modules.common_msgs.simulation_msgs.grading_condition_pb2'})
_sym_db.RegisterMessage(GradePlanning)
LogicalCondition = _reflection.GeneratedProtocolMessageType('LogicalCondition', (_message.Message,), {'DESCRIPTOR': _LOGICALCONDITION, '__module__': 'modules.common_msgs.simulation_msgs.grading_condition_pb2'})
_sym_db.RegisterMessage(LogicalCondition)
SpeedCondition = _reflection.GeneratedProtocolMessageType('SpeedCondition', (_message.Message,), {'DESCRIPTOR': _SPEEDCONDITION, '__module__': 'modules.common_msgs.simulation_msgs.grading_condition_pb2'})
_sym_db.RegisterMessage(SpeedCondition)
CentripetalAccelerationCondition = _reflection.GeneratedProtocolMessageType('CentripetalAccelerationCondition', (_message.Message,), {'DESCRIPTOR': _CENTRIPETALACCELERATIONCONDITION, '__module__': 'modules.common_msgs.simulation_msgs.grading_condition_pb2'})
_sym_db.RegisterMessage(CentripetalAccelerationCondition)
AccelerationCondition = _reflection.GeneratedProtocolMessageType('AccelerationCondition', (_message.Message,), {'DESCRIPTOR': _ACCELERATIONCONDITION, '__module__': 'modules.common_msgs.simulation_msgs.grading_condition_pb2'})
_sym_db.RegisterMessage(AccelerationCondition)
JerkCondition = _reflection.GeneratedProtocolMessageType('JerkCondition', (_message.Message,), {'DESCRIPTOR': _JERKCONDITION, '__module__': 'modules.common_msgs.simulation_msgs.grading_condition_pb2'})
_sym_db.RegisterMessage(JerkCondition)
SpinCondition = _reflection.GeneratedProtocolMessageType('SpinCondition', (_message.Message,), {'DESCRIPTOR': _SPINCONDITION, '__module__': 'modules.common_msgs.simulation_msgs.grading_condition_pb2'})
_sym_db.RegisterMessage(SpinCondition)
ObjectOverlapCondition = _reflection.GeneratedProtocolMessageType('ObjectOverlapCondition', (_message.Message,), {'DESCRIPTOR': _OBJECTOVERLAPCONDITION, '__module__': 'modules.common_msgs.simulation_msgs.grading_condition_pb2'})
_sym_db.RegisterMessage(ObjectOverlapCondition)
RegionOverlapCondition = _reflection.GeneratedProtocolMessageType('RegionOverlapCondition', (_message.Message,), {'DESCRIPTOR': _REGIONOVERLAPCONDITION, '__module__': 'modules.common_msgs.simulation_msgs.grading_condition_pb2'})
_sym_db.RegisterMessage(RegionOverlapCondition)
RegionOverlapLWCondition = _reflection.GeneratedProtocolMessageType('RegionOverlapLWCondition', (_message.Message,), {'DESCRIPTOR': _REGIONOVERLAPLWCONDITION, '__module__': 'modules.common_msgs.simulation_msgs.grading_condition_pb2'})
_sym_db.RegisterMessage(RegionOverlapLWCondition)
OnRoadCondition = _reflection.GeneratedProtocolMessageType('OnRoadCondition', (_message.Message,), {'DESCRIPTOR': _ONROADCONDITION, '__module__': 'modules.common_msgs.simulation_msgs.grading_condition_pb2'})
_sym_db.RegisterMessage(OnRoadCondition)
RunRedLightCondition = _reflection.GeneratedProtocolMessageType('RunRedLightCondition', (_message.Message,), {'DESCRIPTOR': _RUNREDLIGHTCONDITION, '__module__': 'modules.common_msgs.simulation_msgs.grading_condition_pb2'})
_sym_db.RegisterMessage(RunRedLightCondition)
RedLightStopCondition = _reflection.GeneratedProtocolMessageType('RedLightStopCondition', (_message.Message,), {'DESCRIPTOR': _REDLIGHTSTOPCONDITION, '__module__': 'modules.common_msgs.simulation_msgs.grading_condition_pb2'})
_sym_db.RegisterMessage(RedLightStopCondition)
ChangeLaneAtJunctionCondition = _reflection.GeneratedProtocolMessageType('ChangeLaneAtJunctionCondition', (_message.Message,), {'DESCRIPTOR': _CHANGELANEATJUNCTIONCONDITION, '__module__': 'modules.common_msgs.simulation_msgs.grading_condition_pb2'})
_sym_db.RegisterMessage(ChangeLaneAtJunctionCondition)
RoutingCondition = _reflection.GeneratedProtocolMessageType('RoutingCondition', (_message.Message,), {'DESCRIPTOR': _ROUTINGCONDITION, '__module__': 'modules.common_msgs.simulation_msgs.grading_condition_pb2'})
_sym_db.RegisterMessage(RoutingCondition)
CrosswalkYieldCondition = _reflection.GeneratedProtocolMessageType('CrosswalkYieldCondition', (_message.Message,), {'DESCRIPTOR': _CROSSWALKYIELDCONDITION, '__module__': 'modules.common_msgs.simulation_msgs.grading_condition_pb2'})
_sym_db.RegisterMessage(CrosswalkYieldCondition)
CrosswalkStopCondition = _reflection.GeneratedProtocolMessageType('CrosswalkStopCondition', (_message.Message,), {'DESCRIPTOR': _CROSSWALKSTOPCONDITION, '__module__': 'modules.common_msgs.simulation_msgs.grading_condition_pb2'})
_sym_db.RegisterMessage(CrosswalkStopCondition)
AbnormalStopCondition = _reflection.GeneratedProtocolMessageType('AbnormalStopCondition', (_message.Message,), {'DESCRIPTOR': _ABNORMALSTOPCONDITION, '__module__': 'modules.common_msgs.simulation_msgs.grading_condition_pb2'})
_sym_db.RegisterMessage(AbnormalStopCondition)
BrakeTapCondition = _reflection.GeneratedProtocolMessageType('BrakeTapCondition', (_message.Message,), {'DESCRIPTOR': _BRAKETAPCONDITION, '__module__': 'modules.common_msgs.simulation_msgs.grading_condition_pb2'})
_sym_db.RegisterMessage(BrakeTapCondition)
RunStopSignCondition = _reflection.GeneratedProtocolMessageType('RunStopSignCondition', (_message.Message,), {'DESCRIPTOR': _RUNSTOPSIGNCONDITION, '__module__': 'modules.common_msgs.simulation_msgs.grading_condition_pb2'})
_sym_db.RegisterMessage(RunStopSignCondition)
CheckpointCondition = _reflection.GeneratedProtocolMessageType('CheckpointCondition', (_message.Message,), {'DESCRIPTOR': _CHECKPOINTCONDITION, '__module__': 'modules.common_msgs.simulation_msgs.grading_condition_pb2'})
_sym_db.RegisterMessage(CheckpointCondition)
DistToEndCondition = _reflection.GeneratedProtocolMessageType('DistToEndCondition', (_message.Message,), {'DESCRIPTOR': _DISTTOENDCONDITION, '__module__': 'modules.common_msgs.simulation_msgs.grading_condition_pb2'})
_sym_db.RegisterMessage(DistToEndCondition)
DistToLaneCenterCondition = _reflection.GeneratedProtocolMessageType('DistToLaneCenterCondition', (_message.Message,), {'DESCRIPTOR': _DISTTOLANECENTERCONDITION, '__module__': 'modules.common_msgs.simulation_msgs.grading_condition_pb2'})
_sym_db.RegisterMessage(DistToLaneCenterCondition)
TimeLimitCondition = _reflection.GeneratedProtocolMessageType('TimeLimitCondition', (_message.Message,), {'DESCRIPTOR': _TIMELIMITCONDITION, '__module__': 'modules.common_msgs.simulation_msgs.grading_condition_pb2'})
_sym_db.RegisterMessage(TimeLimitCondition)
SpeedbumpLimitCondition = _reflection.GeneratedProtocolMessageType('SpeedbumpLimitCondition', (_message.Message,), {'DESCRIPTOR': _SPEEDBUMPLIMITCONDITION, '__module__': 'modules.common_msgs.simulation_msgs.grading_condition_pb2'})
_sym_db.RegisterMessage(SpeedbumpLimitCondition)
WorkingZoneAvoidLimitCondition = _reflection.GeneratedProtocolMessageType('WorkingZoneAvoidLimitCondition', (_message.Message,), {'DESCRIPTOR': _WORKINGZONEAVOIDLIMITCONDITION, '__module__': 'modules.common_msgs.simulation_msgs.grading_condition_pb2'})
_sym_db.RegisterMessage(WorkingZoneAvoidLimitCondition)
LimitedTimeParkingCondition = _reflection.GeneratedProtocolMessageType('LimitedTimeParkingCondition', (_message.Message,), {'DESCRIPTOR': _LIMITEDTIMEPARKINGCONDITION, '__module__': 'modules.common_msgs.simulation_msgs.grading_condition_pb2'})
_sym_db.RegisterMessage(LimitedTimeParkingCondition)
FollowAndBypassCondition = _reflection.GeneratedProtocolMessageType('FollowAndBypassCondition', (_message.Message,), {'DESCRIPTOR': _FOLLOWANDBYPASSCONDITION, '__module__': 'modules.common_msgs.simulation_msgs.grading_condition_pb2'})
_sym_db.RegisterMessage(FollowAndBypassCondition)
ObstacleBypassCondition = _reflection.GeneratedProtocolMessageType('ObstacleBypassCondition', (_message.Message,), {'DESCRIPTOR': _OBSTACLEBYPASSCONDITION, '__module__': 'modules.common_msgs.simulation_msgs.grading_condition_pb2'})
_sym_db.RegisterMessage(ObstacleBypassCondition)
AntiCheatingCondition = _reflection.GeneratedProtocolMessageType('AntiCheatingCondition', (_message.Message,), {'DESCRIPTOR': _ANTICHEATINGCONDITION, '__module__': 'modules.common_msgs.simulation_msgs.grading_condition_pb2'})
_sym_db.RegisterMessage(AntiCheatingCondition)
KeyPoint = _reflection.GeneratedProtocolMessageType('KeyPoint', (_message.Message,), {'DESCRIPTOR': _KEYPOINT, '__module__': 'modules.common_msgs.simulation_msgs.grading_condition_pb2'})
_sym_db.RegisterMessage(KeyPoint)
KeyPointCondition = _reflection.GeneratedProtocolMessageType('KeyPointCondition', (_message.Message,), {'DESCRIPTOR': _KEYPOINTCONDITION, '__module__': 'modules.common_msgs.simulation_msgs.grading_condition_pb2'})
_sym_db.RegisterMessage(KeyPointCondition)
if _descriptor._USE_C_DESCRIPTORS == False:
    DESCRIPTOR._options = None
    _REGIONOVERLAPCONDITION.fields_by_name['region_corner_xy']._options = None
    _REGIONOVERLAPCONDITION.fields_by_name['region_corner_xy']._serialized_options = b'\x10\x01'
    _CONDITION._serialized_start = 132
    _CONDITION._serialized_end = 2522
    _GRADEPLANNING._serialized_start = 2524
    _GRADEPLANNING._serialized_end = 2633
    _LOGICALCONDITION._serialized_start = 2636
    _LOGICALCONDITION._serialized_end = 2855
    _LOGICALCONDITION_OPERATORTYPE._serialized_start = 2782
    _LOGICALCONDITION_OPERATORTYPE._serialized_end = 2855
    _SPEEDCONDITION._serialized_start = 2858
    _SPEEDCONDITION._serialized_end = 3002
    _CENTRIPETALACCELERATIONCONDITION._serialized_start = 3005
    _CENTRIPETALACCELERATIONCONDITION._serialized_end = 3177
    _ACCELERATIONCONDITION._serialized_start = 3180
    _ACCELERATIONCONDITION._serialized_end = 3353
    _JERKCONDITION._serialized_start = 3355
    _JERKCONDITION._serialized_end = 3439
    _SPINCONDITION._serialized_start = 3441
    _SPINCONDITION._serialized_end = 3525
    _OBJECTOVERLAPCONDITION._serialized_start = 3528
    _OBJECTOVERLAPCONDITION._serialized_end = 3820
    _OBJECTOVERLAPCONDITION_DIRECTIONTYPE._serialized_start = 3769
    _OBJECTOVERLAPCONDITION_DIRECTIONTYPE._serialized_end = 3820
    _REGIONOVERLAPCONDITION._serialized_start = 3823
    _REGIONOVERLAPCONDITION._serialized_end = 3971
    _REGIONOVERLAPLWCONDITION._serialized_start = 3974
    _REGIONOVERLAPLWCONDITION._serialized_end = 4130
    _ONROADCONDITION._serialized_start = 4132
    _ONROADCONDITION._serialized_end = 4209
    _RUNREDLIGHTCONDITION._serialized_start = 4211
    _RUNREDLIGHTCONDITION._serialized_end = 4259
    _REDLIGHTSTOPCONDITION._serialized_start = 4262
    _REDLIGHTSTOPCONDITION._serialized_end = 4392
    _CHANGELANEATJUNCTIONCONDITION._serialized_start = 4394
    _CHANGELANEATJUNCTIONCONDITION._serialized_end = 4425
    _ROUTINGCONDITION._serialized_start = 4427
    _ROUTINGCONDITION._serialized_end = 4445
    _CROSSWALKYIELDCONDITION._serialized_start = 4447
    _CROSSWALKYIELDCONDITION._serialized_end = 4472
    _CROSSWALKSTOPCONDITION._serialized_start = 4475
    _CROSSWALKSTOPCONDITION._serialized_end = 4608
    _ABNORMALSTOPCONDITION._serialized_start = 4610
    _ABNORMALSTOPCONDITION._serialized_end = 4698
    _BRAKETAPCONDITION._serialized_start = 4700
    _BRAKETAPCONDITION._serialized_end = 4769
    _RUNSTOPSIGNCONDITION._serialized_start = 4771
    _RUNSTOPSIGNCONDITION._serialized_end = 4814
    _CHECKPOINTCONDITION._serialized_start = 4816
    _CHECKPOINTCONDITION._serialized_end = 4887
    _DISTTOENDCONDITION._serialized_start = 4889
    _DISTTOENDCONDITION._serialized_end = 4909
    _DISTTOLANECENTERCONDITION._serialized_start = 4911
    _DISTTOLANECENTERCONDITION._serialized_end = 4938
    _TIMELIMITCONDITION._serialized_start = 4940
    _TIMELIMITCONDITION._serialized_end = 5003
    _SPEEDBUMPLIMITCONDITION._serialized_start = 5006
    _SPEEDBUMPLIMITCONDITION._serialized_end = 5176
    _WORKINGZONEAVOIDLIMITCONDITION._serialized_start = 5179
    _WORKINGZONEAVOIDLIMITCONDITION._serialized_end = 5379
    _LIMITEDTIMEPARKINGCONDITION._serialized_start = 5382
    _LIMITEDTIMEPARKINGCONDITION._serialized_end = 5510
    _FOLLOWANDBYPASSCONDITION._serialized_start = 5513
    _FOLLOWANDBYPASSCONDITION._serialized_end = 5699
    _OBSTACLEBYPASSCONDITION._serialized_start = 5702
    _OBSTACLEBYPASSCONDITION._serialized_end = 5901
    _ANTICHEATINGCONDITION._serialized_start = 5903
    _ANTICHEATINGCONDITION._serialized_end = 5952
    _KEYPOINT._serialized_start = 5954
    _KEYPOINT._serialized_end = 6019
    _KEYPOINTCONDITION._serialized_start = 6022
    _KEYPOINTCONDITION._serialized_end = 6154