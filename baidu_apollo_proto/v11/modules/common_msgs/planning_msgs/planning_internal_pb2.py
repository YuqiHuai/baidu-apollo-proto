"""Generated protocol buffer code."""
from google.protobuf.internal import enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
_sym_db = _symbol_database.Default()
from ....modules.common_msgs.basic_msgs import geometry_pb2 as modules_dot_common__msgs_dot_basic__msgs_dot_geometry__pb2
from ....modules.common_msgs.basic_msgs import header_pb2 as modules_dot_common__msgs_dot_basic__msgs_dot_header__pb2
from ....modules.common_msgs.basic_msgs import pnc_point_pb2 as modules_dot_common__msgs_dot_basic__msgs_dot_pnc__point__pb2
from ....modules.common_msgs.chassis_msgs import chassis_pb2 as modules_dot_common__msgs_dot_chassis__msgs_dot_chassis__pb2
from ....modules.common_msgs.dreamview_msgs import chart_pb2 as modules_dot_common__msgs_dot_dreamview__msgs_dot_chart__pb2
from ....modules.common_msgs.localization_msgs import localization_pb2 as modules_dot_common__msgs_dot_localization__msgs_dot_localization__pb2
from ....modules.common_msgs.perception_msgs import traffic_light_detection_pb2 as modules_dot_common__msgs_dot_perception__msgs_dot_traffic__light__detection__pb2
from ....modules.common_msgs.planning_msgs import decision_pb2 as modules_dot_common__msgs_dot_planning__msgs_dot_decision__pb2
from ....modules.common_msgs.planning_msgs import navigation_pb2 as modules_dot_common__msgs_dot_planning__msgs_dot_navigation__pb2
from ....modules.common_msgs.planning_msgs import sl_boundary_pb2 as modules_dot_common__msgs_dot_planning__msgs_dot_sl__boundary__pb2
from ....modules.common_msgs.routing_msgs import routing_pb2 as modules_dot_common__msgs_dot_routing__msgs_dot_routing__pb2
from ....modules.common_msgs.routing_msgs import geometry_pb2 as modules_dot_common__msgs_dot_routing__msgs_dot_geometry__pb2
from ....modules.common_msgs.map_msgs import map_lane_pb2 as modules_dot_common__msgs_dot_map__msgs_dot_map__lane__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n9modules/common_msgs/planning_msgs/planning_internal.proto\x12\x18apollo.planning_internal\x1a-modules/common_msgs/basic_msgs/geometry.proto\x1a+modules/common_msgs/basic_msgs/header.proto\x1a.modules/common_msgs/basic_msgs/pnc_point.proto\x1a.modules/common_msgs/chassis_msgs/chassis.proto\x1a.modules/common_msgs/dreamview_msgs/chart.proto\x1a8modules/common_msgs/localization_msgs/localization.proto\x1aAmodules/common_msgs/perception_msgs/traffic_light_detection.proto\x1a0modules/common_msgs/planning_msgs/decision.proto\x1a2modules/common_msgs/planning_msgs/navigation.proto\x1a3modules/common_msgs/planning_msgs/sl_boundary.proto\x1a.modules/common_msgs/routing_msgs/routing.proto\x1a/modules/common_msgs/routing_msgs/geometry.proto\x1a+modules/common_msgs/map_msgs/map_lane.proto"F\n\x05Debug\x12=\n\rplanning_data\x18\x02 \x01(\x0b2&.apollo.planning_internal.PlanningData"I\n\tSpeedPlan\x12\x0c\n\x04name\x18\x01 \x01(\t\x12.\n\x0bspeed_point\x18\x02 \x03(\x0b2\x19.apollo.common.SpeedPoint"\x86\x03\n\x14StGraphBoundaryDebug\x12\x0c\n\x04name\x18\x01 \x01(\t\x12(\n\x05point\x18\x02 \x03(\x0b2\x19.apollo.common.SpeedPoint\x12K\n\x04type\x18\x03 \x01(\x0e2=.apollo.planning_internal.StGraphBoundaryDebug.StBoundaryType"\xe8\x01\n\x0eStBoundaryType\x12\x1c\n\x18ST_BOUNDARY_TYPE_UNKNOWN\x10\x01\x12\x19\n\x15ST_BOUNDARY_TYPE_STOP\x10\x02\x12\x1b\n\x17ST_BOUNDARY_TYPE_FOLLOW\x10\x03\x12\x1a\n\x16ST_BOUNDARY_TYPE_YIELD\x10\x04\x12\x1d\n\x19ST_BOUNDARY_TYPE_OVERTAKE\x10\x05\x12\x1f\n\x1bST_BOUNDARY_TYPE_KEEP_CLEAR\x10\x06\x12$\n ST_BOUNDARY_TYPE_DRIVABLE_REGION\x10\x07"\x82\x03\n\x0cSLFrameDebug\x12\x0c\n\x04name\x18\x01 \x01(\t\x12\x11\n\tsampled_s\x18\x02 \x03(\x01\x12#\n\x1bstatic_obstacle_lower_bound\x18\x03 \x03(\x01\x12$\n\x1cdynamic_obstacle_lower_bound\x18\x04 \x03(\x01\x12#\n\x1bstatic_obstacle_upper_bound\x18\x05 \x03(\x01\x12$\n\x1cdynamic_obstacle_upper_bound\x18\x06 \x03(\x01\x12\x17\n\x0fmap_lower_bound\x18\x07 \x03(\x01\x12\x17\n\x0fmap_upper_bound\x18\x08 \x03(\x01\x12\'\n\x07sl_path\x18\t \x03(\x0b2\x16.apollo.common.SLPoint\x12\x1d\n\x15aggregated_boundary_s\x18\n \x03(\x01\x12\x1f\n\x17aggregated_boundary_low\x18\x0b \x03(\x01\x12 \n\x18aggregated_boundary_high\x18\x0c \x03(\x01"\x92\x05\n\x0cSTGraphDebug\x12\x0c\n\x04name\x18\x01 \x01(\t\x12@\n\x08boundary\x18\x02 \x03(\x0b2..apollo.planning_internal.StGraphBoundaryDebug\x12.\n\x0bspeed_limit\x18\x03 \x03(\x0b2\x19.apollo.common.SpeedPoint\x120\n\rspeed_profile\x18\x04 \x03(\x0b2\x19.apollo.common.SpeedPoint\x12W\n\x10speed_constraint\x18\x05 \x01(\x0b2=.apollo.planning_internal.STGraphDebug.STGraphSpeedConstraint\x12W\n\x11kernel_cruise_ref\x18\x06 \x01(\x0b2<.apollo.planning_internal.STGraphDebug.STGraphKernelCuiseRef\x12X\n\x11kernel_follow_ref\x18\x07 \x01(\x0b2=.apollo.planning_internal.STGraphDebug.STGraphKernelFollowRef\x1aM\n\x16STGraphSpeedConstraint\x12\t\n\x01t\x18\x01 \x03(\x01\x12\x13\n\x0blower_bound\x18\x02 \x03(\x01\x12\x13\n\x0bupper_bound\x18\x03 \x03(\x01\x1a9\n\x15STGraphKernelCuiseRef\x12\t\n\x01t\x18\x01 \x03(\x01\x12\x15\n\rcruise_line_s\x18\x02 \x03(\x01\x1a:\n\x16STGraphKernelFollowRef\x12\t\n\x01t\x18\x01 \x03(\x01\x12\x15\n\rfollow_line_s\x18\x02 \x03(\x01"\xad\x02\n\x10SignalLightDebug\x12\x11\n\tadc_speed\x18\x01 \x01(\x01\x12\x13\n\x0badc_front_s\x18\x02 \x01(\x01\x12F\n\x06signal\x18\x03 \x03(\x0b26.apollo.planning_internal.SignalLightDebug.SignalDebug\x1a\xa8\x01\n\x0bSignalDebug\x12\x10\n\x08light_id\x18\x01 \x01(\t\x124\n\x05color\x18\x02 \x01(\x0e2%.apollo.perception.TrafficLight.Color\x12\x14\n\x0clight_stop_s\x18\x03 \x01(\x01\x12\x1d\n\x15adc_stop_deceleration\x18\x04 \x01(\x01\x12\x1c\n\x14is_stop_wall_created\x18\x05 \x01(\x08"Y\n\x0bDecisionTag\x12\x13\n\x0bdecider_tag\x18\x01 \x01(\t\x125\n\x08decision\x18\x02 \x01(\x0b2#.apollo.planning.ObjectDecisionType"\xc0\x01\n\rObstacleDebug\x12\n\n\x02id\x18\x01 \x01(\t\x120\n\x0bsl_boundary\x18\x02 \x01(\x0b2\x1b.apollo.planning.SLBoundary\x12;\n\x0cdecision_tag\x18\x03 \x03(\x0b2%.apollo.planning_internal.DecisionTag\x12\x19\n\x11vertices_x_coords\x18\x04 \x03(\x01\x12\x19\n\x11vertices_y_coords\x18\x05 \x03(\x01"\xd9\x02\n\x12ReferenceLineDebug\x12\n\n\x02id\x18\x01 \x01(\t\x12\x0e\n\x06length\x18\x02 \x01(\x01\x12\x0c\n\x04cost\x18\x03 \x01(\x01\x12\x1b\n\x13is_change_lane_path\x18\x04 \x01(\x08\x12\x13\n\x0bis_drivable\x18\x05 \x01(\x08\x12\x14\n\x0cis_protected\x18\x06 \x01(\x08\x12\x12\n\nis_offroad\x18\x07 \x01(\x08\x12\x18\n\x10minimum_boundary\x18\x08 \x01(\x01\x12\x19\n\raverage_kappa\x18\t \x01(\x01B\x02\x18\x01\x12\x1a\n\x0eaverage_dkappa\x18\n \x01(\x01B\x02\x18\x01\x12\x11\n\tkappa_rms\x18\x0b \x01(\x01\x12\x12\n\ndkappa_rms\x18\x0c \x01(\x01\x12\x15\n\rkappa_max_abs\x18\r \x01(\x01\x12\x16\n\x0edkappa_max_abs\x18\x0e \x01(\x01\x12\x16\n\x0eaverage_offset\x18\x0f \x01(\x01"<\n\x10SampleLayerDebug\x12(\n\x08sl_point\x18\x01 \x03(\x0b2\x16.apollo.common.SLPoint"\x84\x01\n\x10DpPolyGraphDebug\x12@\n\x0csample_layer\x18\x01 \x03(\x0b2*.apollo.planning_internal.SampleLayerDebug\x12.\n\x0emin_cost_point\x18\x02 \x03(\x0b2\x16.apollo.common.SLPoint"\x88\x01\n\rScenarioDebug\x12\x19\n\rscenario_type\x18\x01 \x01(\x05B\x02\x18\x01\x12\x16\n\nstage_type\x18\x02 \x01(\x05B\x02\x18\x01\x12\x0b\n\x03msg\x18\x03 \x01(\t\x12\x1c\n\x14scenario_plugin_type\x18\x04 \x01(\t\x12\x19\n\x11stage_plugin_type\x18\x05 \x01(\t"=\n\x0cTrajectories\x12-\n\ntrajectory\x18\x01 \x03(\x0b2\x19.apollo.common.Trajectory"\xd5\x07\n\x0eOpenSpaceDebug\x12<\n\x0ctrajectories\x18\x01 \x01(\x0b2&.apollo.planning_internal.Trajectories\x12;\n\x15warm_start_trajectory\x18\x02 \x01(\x0b2\x1c.apollo.common.VehicleMotion\x129\n\x13smoothed_trajectory\x18\x03 \x01(\x0b2\x1c.apollo.common.VehicleMotion\x12\x1e\n\x16warm_start_dual_lambda\x18\x04 \x03(\x01\x12\x1b\n\x13warm_start_dual_miu\x18\x05 \x03(\x01\x12\x1d\n\x15optimized_dual_lambda\x18\x06 \x03(\x01\x12\x1a\n\x12optimized_dual_miu\x18\x07 \x03(\x01\x12\x13\n\x0bxy_boundary\x18\x08 \x03(\x01\x12:\n\tobstacles\x18\t \x03(\x0b2\'.apollo.planning_internal.ObstacleDebug\x127\n\x0froi_shift_point\x18\n \x01(\x0b2\x1e.apollo.common.TrajectoryPoint\x121\n\tend_point\x18\x0b \x01(\x0b2\x1e.apollo.common.TrajectoryPoint\x12H\n\x18partitioned_trajectories\x18\x0c \x01(\x0b2&.apollo.planning_internal.Trajectories\x12A\n\x11chosen_trajectory\x18\r \x01(\x0b2&.apollo.planning_internal.Trajectories\x12\x1e\n\x16is_fallback_trajectory\x18\x0e \x01(\x08\x12C\n\x13fallback_trajectory\x18\x0f \x01(\x0b2&.apollo.planning_internal.Trajectories\x12B\n\x1atrajectory_stitching_point\x18\x10 \x01(\x0b2\x1e.apollo.common.TrajectoryPoint\x12>\n\x16future_collision_point\x18\x11 \x01(\x0b2\x1e.apollo.common.TrajectoryPoint\x12\x17\n\x0ctime_latency\x18\x12 \x01(\x01:\x010\x12-\n\x0corigin_point\x18\x13 \x01(\x0b2\x17.apollo.common.PointENU\x12\x1a\n\x12origin_heading_rad\x18\x14 \x01(\x01"\xc3\x01\n\rSmootherDebug\x12\x13\n\x0bis_smoothed\x18\x01 \x01(\x08\x12Q\n\x04type\x18\x02 \x01(\x0e24.apollo.planning_internal.SmootherDebug.SmootherType:\rSMOOTHER_NONE\x12\x0e\n\x06reason\x18\x03 \x01(\t":\n\x0cSmootherType\x12\x11\n\rSMOOTHER_NONE\x10\x01\x12\x17\n\x13SMOOTHER_CLOSE_STOP\x10\x02"\x9d\x01\n\rPullOverDebug\x12)\n\x08position\x18\x01 \x01(\x0b2\x17.apollo.common.PointENU\x12\r\n\x05theta\x18\x02 \x01(\x01\x12\x14\n\x0clength_front\x18\x03 \x01(\x01\x12\x13\n\x0blength_back\x18\x04 \x01(\x01\x12\x12\n\nwidth_left\x18\x05 \x01(\x01\x12\x13\n\x0bwidth_right\x18\x06 \x01(\x01"\xf3\n\n\x0cPlanningData\x12?\n\x0cadc_position\x18\x07 \x01(\x0b2).apollo.localization.LocalizationEstimate\x12\'\n\x07chassis\x18\x08 \x01(\x0b2\x16.apollo.canbus.Chassis\x120\n\x07routing\x18\t \x01(\x0b2\x1f.apollo.routing.RoutingResponse\x122\n\ninit_point\x18\n \x01(\x0b2\x1e.apollo.common.TrajectoryPoint\x12!\n\x04path\x18\x06 \x03(\x0b2\x13.apollo.common.Path\x127\n\nspeed_plan\x18\r \x03(\x0b2#.apollo.planning_internal.SpeedPlan\x128\n\x08st_graph\x18\x0e \x03(\x0b2&.apollo.planning_internal.STGraphDebug\x128\n\x08sl_frame\x18\x0f \x03(\x0b2&.apollo.planning_internal.SLFrameDebug\x120\n\x11prediction_header\x18\x10 \x01(\x0b2\x15.apollo.common.Header\x12@\n\x0csignal_light\x18\x11 \x01(\x0b2*.apollo.planning_internal.SignalLightDebug\x129\n\x08obstacle\x18\x12 \x03(\x0b2\'.apollo.planning_internal.ObstacleDebug\x12D\n\x0ereference_line\x18\x13 \x03(\x0b2,.apollo.planning_internal.ReferenceLineDebug\x12A\n\rdp_poly_graph\x18\x14 \x01(\x0b2*.apollo.planning_internal.DpPolyGraphDebug\x12E\n\x10lattice_st_image\x18\x15 \x01(\x0b2+.apollo.planning_internal.LatticeStTraining\x121\n\x0crelative_map\x18\x16 \x01(\x0b2\x1b.apollo.relative_map.MapMsg\x12S\n\x19auto_tuning_training_data\x18\x17 \x01(\x0b20.apollo.planning_internal.AutoTuningTrainingData\x12\x1c\n\x14front_clear_distance\x18\x18 \x01(\x01\x12&\n\x05chart\x18\x19 \x03(\x0b2\x17.apollo.dreamview.Chart\x129\n\x08scenario\x18\x1a \x01(\x0b2\'.apollo.planning_internal.ScenarioDebug\x12<\n\nopen_space\x18\x1b \x01(\x0b2(.apollo.planning_internal.OpenSpaceDebug\x129\n\x08smoother\x18\x1c \x01(\x0b2\'.apollo.planning_internal.SmootherDebug\x12:\n\tpull_over\x18\x1d \x01(\x0b2\'.apollo.planning_internal.PullOverDebug\x12@\n\x0chybrid_model\x18\x1e \x01(\x0b2*.apollo.planning_internal.HybridModelDebug\x12D\n\x11adc_driving_state\x18\x1f \x01(\x0b2).apollo.planning_internal.ADCDrivingState"G\n\x0eLatticeStPixel\x12\t\n\x01s\x18\x01 \x01(\x05\x12\t\n\x01t\x18\x02 \x01(\x05\x12\t\n\x01r\x18\x03 \x01(\r\x12\t\n\x01g\x18\x04 \x01(\r\x12\t\n\x01b\x18\x05 \x01(\r"\xc9\x01\n\x11LatticeStTraining\x127\n\x05pixel\x18\x01 \x03(\x0b2(.apollo.planning_internal.LatticeStPixel\x12\x11\n\ttimestamp\x18\x02 \x01(\x01\x12\x12\n\nannotation\x18\x03 \x01(\t\x12\x13\n\x0bnum_s_grids\x18\x04 \x01(\r\x12\x13\n\x0bnum_t_grids\x18\x05 \x01(\r\x12\x14\n\x0cs_resolution\x18\x06 \x01(\x01\x12\x14\n\x0ct_resolution\x18\x07 \x01(\x01"(\n\x0eCostComponents\x12\x16\n\x0ecost_component\x18\x01 \x03(\x01"\xa2\x01\n\x16AutoTuningTrainingData\x12C\n\x11teacher_component\x18\x01 \x01(\x0b2(.apollo.planning_internal.CostComponents\x12C\n\x11student_component\x18\x02 \x01(\x0b2(.apollo.planning_internal.CostComponents"N\n\x19CloudReferenceLineRequest\x121\n\x0clane_segment\x18\x01 \x03(\x0b2\x1b.apollo.routing.LaneSegment"T\n CloudReferenceLineRoutingRequest\x120\n\x07routing\x18\x01 \x01(\x0b2\x1f.apollo.routing.RoutingResponse"B\n\x1aCloudReferenceLineResponse\x12$\n\x07segment\x18\x01 \x03(\x0b2\x13.apollo.common.Path"\xcb\x01\n\x10HybridModelDebug\x12*\n\x1busing_learning_model_output\x18\x01 \x01(\x08:\x05false\x12)\n!learning_model_output_usage_ratio\x18\x02 \x01(\x01\x12)\n!learning_model_output_fail_reason\x18\x03 \x01(\t\x125\n\x18evaluated_path_reference\x18\x04 \x01(\x0b2\x13.apollo.common.Path"\xe5\x01\n\x12NudgeObstacleDebug\x12D\n\x04type\x18\x01 \x01(\x0e26.apollo.planning_internal.NudgeObstacleDebug.NudgeType\x129\n\x08obstacle\x18\x02 \x01(\x0b2\'.apollo.planning_internal.ObstacleDebug\x12\x12\n\nis_blocked\x18\x03 \x01(\x08":\n\tNudgeType\x12\x0c\n\x08NO_NUDGE\x10\x01\x12\x0e\n\nLEFT_NUDGE\x10\x02\x12\x0f\n\x0bRIGHT_NUDGE\x10\x03"`\n\x0cLaneTurnInfo\x127\n\tturn_type\x18\x01 \x01(\x0e2\x1b.apollo.hdmap.Lane.LaneTurn:\x07NO_TURN\x12\x17\n\x0bdis_to_turn\x18\x02 \x01(\x01:\x02-1"\x84\x04\n\x0fADCDrivingState\x12\x0f\n\x07lane_id\x18\x01 \x01(\t\x12\x11\n\ts_in_lane\x18\x02 \x01(\x01\x12\x1f\n\x17distance_to_destination\x18\x03 \x01(\x01\x12M\n\x10lane_change_type\x18\x04 \x01(\x0e2(.apollo.planning_internal.LaneChangeType:\tNO_CHANGE\x12M\n\x10lane_borrow_type\x18\x05 \x01(\x0e2(.apollo.planning_internal.LaneBorrowType:\tNO_BORROW\x122\n\rcur_turn_info\x18\x06 \x01(\x0e2\x1b.apollo.hdmap.Lane.LaneTurn\x12>\n\x0enext_turn_info\x18\x07 \x01(\x0b2&.apollo.planning_internal.LaneTurnInfo\x12\x1d\n\x0eis_in_junction\x18\x08 \x01(\x08:\x05false\x12\x1a\n\x0bis_fallback\x18\t \x01(\x08:\x05false\x12\x19\n\nis_nudging\x18\n \x01(\x08:\x05false\x12D\n\x0enudge_obstacle\x18\x0b \x03(\x0b2,.apollo.planning_internal.NudgeObstacleDebug*B\n\x0eLaneChangeType\x12\r\n\tNO_CHANGE\x10\x01\x12\x0f\n\x0bLEFT_CHANGE\x10\x02\x12\x10\n\x0cRIGHT_CHANGE\x10\x03*B\n\x0eLaneBorrowType\x12\r\n\tNO_BORROW\x10\x01\x12\x0f\n\x0bLEFT_BORROW\x10\x02\x12\x10\n\x0cRIGHT_BORROW\x10\x03')
_LANECHANGETYPE = DESCRIPTOR.enum_types_by_name['LaneChangeType']
LaneChangeType = enum_type_wrapper.EnumTypeWrapper(_LANECHANGETYPE)
_LANEBORROWTYPE = DESCRIPTOR.enum_types_by_name['LaneBorrowType']
LaneBorrowType = enum_type_wrapper.EnumTypeWrapper(_LANEBORROWTYPE)
NO_CHANGE = 1
LEFT_CHANGE = 2
RIGHT_CHANGE = 3
NO_BORROW = 1
LEFT_BORROW = 2
RIGHT_BORROW = 3
_DEBUG = DESCRIPTOR.message_types_by_name['Debug']
_SPEEDPLAN = DESCRIPTOR.message_types_by_name['SpeedPlan']
_STGRAPHBOUNDARYDEBUG = DESCRIPTOR.message_types_by_name['StGraphBoundaryDebug']
_SLFRAMEDEBUG = DESCRIPTOR.message_types_by_name['SLFrameDebug']
_STGRAPHDEBUG = DESCRIPTOR.message_types_by_name['STGraphDebug']
_STGRAPHDEBUG_STGRAPHSPEEDCONSTRAINT = _STGRAPHDEBUG.nested_types_by_name['STGraphSpeedConstraint']
_STGRAPHDEBUG_STGRAPHKERNELCUISEREF = _STGRAPHDEBUG.nested_types_by_name['STGraphKernelCuiseRef']
_STGRAPHDEBUG_STGRAPHKERNELFOLLOWREF = _STGRAPHDEBUG.nested_types_by_name['STGraphKernelFollowRef']
_SIGNALLIGHTDEBUG = DESCRIPTOR.message_types_by_name['SignalLightDebug']
_SIGNALLIGHTDEBUG_SIGNALDEBUG = _SIGNALLIGHTDEBUG.nested_types_by_name['SignalDebug']
_DECISIONTAG = DESCRIPTOR.message_types_by_name['DecisionTag']
_OBSTACLEDEBUG = DESCRIPTOR.message_types_by_name['ObstacleDebug']
_REFERENCELINEDEBUG = DESCRIPTOR.message_types_by_name['ReferenceLineDebug']
_SAMPLELAYERDEBUG = DESCRIPTOR.message_types_by_name['SampleLayerDebug']
_DPPOLYGRAPHDEBUG = DESCRIPTOR.message_types_by_name['DpPolyGraphDebug']
_SCENARIODEBUG = DESCRIPTOR.message_types_by_name['ScenarioDebug']
_TRAJECTORIES = DESCRIPTOR.message_types_by_name['Trajectories']
_OPENSPACEDEBUG = DESCRIPTOR.message_types_by_name['OpenSpaceDebug']
_SMOOTHERDEBUG = DESCRIPTOR.message_types_by_name['SmootherDebug']
_PULLOVERDEBUG = DESCRIPTOR.message_types_by_name['PullOverDebug']
_PLANNINGDATA = DESCRIPTOR.message_types_by_name['PlanningData']
_LATTICESTPIXEL = DESCRIPTOR.message_types_by_name['LatticeStPixel']
_LATTICESTTRAINING = DESCRIPTOR.message_types_by_name['LatticeStTraining']
_COSTCOMPONENTS = DESCRIPTOR.message_types_by_name['CostComponents']
_AUTOTUNINGTRAININGDATA = DESCRIPTOR.message_types_by_name['AutoTuningTrainingData']
_CLOUDREFERENCELINEREQUEST = DESCRIPTOR.message_types_by_name['CloudReferenceLineRequest']
_CLOUDREFERENCELINEROUTINGREQUEST = DESCRIPTOR.message_types_by_name['CloudReferenceLineRoutingRequest']
_CLOUDREFERENCELINERESPONSE = DESCRIPTOR.message_types_by_name['CloudReferenceLineResponse']
_HYBRIDMODELDEBUG = DESCRIPTOR.message_types_by_name['HybridModelDebug']
_NUDGEOBSTACLEDEBUG = DESCRIPTOR.message_types_by_name['NudgeObstacleDebug']
_LANETURNINFO = DESCRIPTOR.message_types_by_name['LaneTurnInfo']
_ADCDRIVINGSTATE = DESCRIPTOR.message_types_by_name['ADCDrivingState']
_STGRAPHBOUNDARYDEBUG_STBOUNDARYTYPE = _STGRAPHBOUNDARYDEBUG.enum_types_by_name['StBoundaryType']
_SMOOTHERDEBUG_SMOOTHERTYPE = _SMOOTHERDEBUG.enum_types_by_name['SmootherType']
_NUDGEOBSTACLEDEBUG_NUDGETYPE = _NUDGEOBSTACLEDEBUG.enum_types_by_name['NudgeType']
Debug = _reflection.GeneratedProtocolMessageType('Debug', (_message.Message,), {'DESCRIPTOR': _DEBUG, '__module__': 'modules.common_msgs.planning_msgs.planning_internal_pb2'})
_sym_db.RegisterMessage(Debug)
SpeedPlan = _reflection.GeneratedProtocolMessageType('SpeedPlan', (_message.Message,), {'DESCRIPTOR': _SPEEDPLAN, '__module__': 'modules.common_msgs.planning_msgs.planning_internal_pb2'})
_sym_db.RegisterMessage(SpeedPlan)
StGraphBoundaryDebug = _reflection.GeneratedProtocolMessageType('StGraphBoundaryDebug', (_message.Message,), {'DESCRIPTOR': _STGRAPHBOUNDARYDEBUG, '__module__': 'modules.common_msgs.planning_msgs.planning_internal_pb2'})
_sym_db.RegisterMessage(StGraphBoundaryDebug)
SLFrameDebug = _reflection.GeneratedProtocolMessageType('SLFrameDebug', (_message.Message,), {'DESCRIPTOR': _SLFRAMEDEBUG, '__module__': 'modules.common_msgs.planning_msgs.planning_internal_pb2'})
_sym_db.RegisterMessage(SLFrameDebug)
STGraphDebug = _reflection.GeneratedProtocolMessageType('STGraphDebug', (_message.Message,), {'STGraphSpeedConstraint': _reflection.GeneratedProtocolMessageType('STGraphSpeedConstraint', (_message.Message,), {'DESCRIPTOR': _STGRAPHDEBUG_STGRAPHSPEEDCONSTRAINT, '__module__': 'modules.common_msgs.planning_msgs.planning_internal_pb2'}), 'STGraphKernelCuiseRef': _reflection.GeneratedProtocolMessageType('STGraphKernelCuiseRef', (_message.Message,), {'DESCRIPTOR': _STGRAPHDEBUG_STGRAPHKERNELCUISEREF, '__module__': 'modules.common_msgs.planning_msgs.planning_internal_pb2'}), 'STGraphKernelFollowRef': _reflection.GeneratedProtocolMessageType('STGraphKernelFollowRef', (_message.Message,), {'DESCRIPTOR': _STGRAPHDEBUG_STGRAPHKERNELFOLLOWREF, '__module__': 'modules.common_msgs.planning_msgs.planning_internal_pb2'}), 'DESCRIPTOR': _STGRAPHDEBUG, '__module__': 'modules.common_msgs.planning_msgs.planning_internal_pb2'})
_sym_db.RegisterMessage(STGraphDebug)
_sym_db.RegisterMessage(STGraphDebug.STGraphSpeedConstraint)
_sym_db.RegisterMessage(STGraphDebug.STGraphKernelCuiseRef)
_sym_db.RegisterMessage(STGraphDebug.STGraphKernelFollowRef)
SignalLightDebug = _reflection.GeneratedProtocolMessageType('SignalLightDebug', (_message.Message,), {'SignalDebug': _reflection.GeneratedProtocolMessageType('SignalDebug', (_message.Message,), {'DESCRIPTOR': _SIGNALLIGHTDEBUG_SIGNALDEBUG, '__module__': 'modules.common_msgs.planning_msgs.planning_internal_pb2'}), 'DESCRIPTOR': _SIGNALLIGHTDEBUG, '__module__': 'modules.common_msgs.planning_msgs.planning_internal_pb2'})
_sym_db.RegisterMessage(SignalLightDebug)
_sym_db.RegisterMessage(SignalLightDebug.SignalDebug)
DecisionTag = _reflection.GeneratedProtocolMessageType('DecisionTag', (_message.Message,), {'DESCRIPTOR': _DECISIONTAG, '__module__': 'modules.common_msgs.planning_msgs.planning_internal_pb2'})
_sym_db.RegisterMessage(DecisionTag)
ObstacleDebug = _reflection.GeneratedProtocolMessageType('ObstacleDebug', (_message.Message,), {'DESCRIPTOR': _OBSTACLEDEBUG, '__module__': 'modules.common_msgs.planning_msgs.planning_internal_pb2'})
_sym_db.RegisterMessage(ObstacleDebug)
ReferenceLineDebug = _reflection.GeneratedProtocolMessageType('ReferenceLineDebug', (_message.Message,), {'DESCRIPTOR': _REFERENCELINEDEBUG, '__module__': 'modules.common_msgs.planning_msgs.planning_internal_pb2'})
_sym_db.RegisterMessage(ReferenceLineDebug)
SampleLayerDebug = _reflection.GeneratedProtocolMessageType('SampleLayerDebug', (_message.Message,), {'DESCRIPTOR': _SAMPLELAYERDEBUG, '__module__': 'modules.common_msgs.planning_msgs.planning_internal_pb2'})
_sym_db.RegisterMessage(SampleLayerDebug)
DpPolyGraphDebug = _reflection.GeneratedProtocolMessageType('DpPolyGraphDebug', (_message.Message,), {'DESCRIPTOR': _DPPOLYGRAPHDEBUG, '__module__': 'modules.common_msgs.planning_msgs.planning_internal_pb2'})
_sym_db.RegisterMessage(DpPolyGraphDebug)
ScenarioDebug = _reflection.GeneratedProtocolMessageType('ScenarioDebug', (_message.Message,), {'DESCRIPTOR': _SCENARIODEBUG, '__module__': 'modules.common_msgs.planning_msgs.planning_internal_pb2'})
_sym_db.RegisterMessage(ScenarioDebug)
Trajectories = _reflection.GeneratedProtocolMessageType('Trajectories', (_message.Message,), {'DESCRIPTOR': _TRAJECTORIES, '__module__': 'modules.common_msgs.planning_msgs.planning_internal_pb2'})
_sym_db.RegisterMessage(Trajectories)
OpenSpaceDebug = _reflection.GeneratedProtocolMessageType('OpenSpaceDebug', (_message.Message,), {'DESCRIPTOR': _OPENSPACEDEBUG, '__module__': 'modules.common_msgs.planning_msgs.planning_internal_pb2'})
_sym_db.RegisterMessage(OpenSpaceDebug)
SmootherDebug = _reflection.GeneratedProtocolMessageType('SmootherDebug', (_message.Message,), {'DESCRIPTOR': _SMOOTHERDEBUG, '__module__': 'modules.common_msgs.planning_msgs.planning_internal_pb2'})
_sym_db.RegisterMessage(SmootherDebug)
PullOverDebug = _reflection.GeneratedProtocolMessageType('PullOverDebug', (_message.Message,), {'DESCRIPTOR': _PULLOVERDEBUG, '__module__': 'modules.common_msgs.planning_msgs.planning_internal_pb2'})
_sym_db.RegisterMessage(PullOverDebug)
PlanningData = _reflection.GeneratedProtocolMessageType('PlanningData', (_message.Message,), {'DESCRIPTOR': _PLANNINGDATA, '__module__': 'modules.common_msgs.planning_msgs.planning_internal_pb2'})
_sym_db.RegisterMessage(PlanningData)
LatticeStPixel = _reflection.GeneratedProtocolMessageType('LatticeStPixel', (_message.Message,), {'DESCRIPTOR': _LATTICESTPIXEL, '__module__': 'modules.common_msgs.planning_msgs.planning_internal_pb2'})
_sym_db.RegisterMessage(LatticeStPixel)
LatticeStTraining = _reflection.GeneratedProtocolMessageType('LatticeStTraining', (_message.Message,), {'DESCRIPTOR': _LATTICESTTRAINING, '__module__': 'modules.common_msgs.planning_msgs.planning_internal_pb2'})
_sym_db.RegisterMessage(LatticeStTraining)
CostComponents = _reflection.GeneratedProtocolMessageType('CostComponents', (_message.Message,), {'DESCRIPTOR': _COSTCOMPONENTS, '__module__': 'modules.common_msgs.planning_msgs.planning_internal_pb2'})
_sym_db.RegisterMessage(CostComponents)
AutoTuningTrainingData = _reflection.GeneratedProtocolMessageType('AutoTuningTrainingData', (_message.Message,), {'DESCRIPTOR': _AUTOTUNINGTRAININGDATA, '__module__': 'modules.common_msgs.planning_msgs.planning_internal_pb2'})
_sym_db.RegisterMessage(AutoTuningTrainingData)
CloudReferenceLineRequest = _reflection.GeneratedProtocolMessageType('CloudReferenceLineRequest', (_message.Message,), {'DESCRIPTOR': _CLOUDREFERENCELINEREQUEST, '__module__': 'modules.common_msgs.planning_msgs.planning_internal_pb2'})
_sym_db.RegisterMessage(CloudReferenceLineRequest)
CloudReferenceLineRoutingRequest = _reflection.GeneratedProtocolMessageType('CloudReferenceLineRoutingRequest', (_message.Message,), {'DESCRIPTOR': _CLOUDREFERENCELINEROUTINGREQUEST, '__module__': 'modules.common_msgs.planning_msgs.planning_internal_pb2'})
_sym_db.RegisterMessage(CloudReferenceLineRoutingRequest)
CloudReferenceLineResponse = _reflection.GeneratedProtocolMessageType('CloudReferenceLineResponse', (_message.Message,), {'DESCRIPTOR': _CLOUDREFERENCELINERESPONSE, '__module__': 'modules.common_msgs.planning_msgs.planning_internal_pb2'})
_sym_db.RegisterMessage(CloudReferenceLineResponse)
HybridModelDebug = _reflection.GeneratedProtocolMessageType('HybridModelDebug', (_message.Message,), {'DESCRIPTOR': _HYBRIDMODELDEBUG, '__module__': 'modules.common_msgs.planning_msgs.planning_internal_pb2'})
_sym_db.RegisterMessage(HybridModelDebug)
NudgeObstacleDebug = _reflection.GeneratedProtocolMessageType('NudgeObstacleDebug', (_message.Message,), {'DESCRIPTOR': _NUDGEOBSTACLEDEBUG, '__module__': 'modules.common_msgs.planning_msgs.planning_internal_pb2'})
_sym_db.RegisterMessage(NudgeObstacleDebug)
LaneTurnInfo = _reflection.GeneratedProtocolMessageType('LaneTurnInfo', (_message.Message,), {'DESCRIPTOR': _LANETURNINFO, '__module__': 'modules.common_msgs.planning_msgs.planning_internal_pb2'})
_sym_db.RegisterMessage(LaneTurnInfo)
ADCDrivingState = _reflection.GeneratedProtocolMessageType('ADCDrivingState', (_message.Message,), {'DESCRIPTOR': _ADCDRIVINGSTATE, '__module__': 'modules.common_msgs.planning_msgs.planning_internal_pb2'})
_sym_db.RegisterMessage(ADCDrivingState)
if _descriptor._USE_C_DESCRIPTORS == False:
    DESCRIPTOR._options = None
    _REFERENCELINEDEBUG.fields_by_name['average_kappa']._options = None
    _REFERENCELINEDEBUG.fields_by_name['average_kappa']._serialized_options = b'\x18\x01'
    _REFERENCELINEDEBUG.fields_by_name['average_dkappa']._options = None
    _REFERENCELINEDEBUG.fields_by_name['average_dkappa']._serialized_options = b'\x18\x01'
    _SCENARIODEBUG.fields_by_name['scenario_type']._options = None
    _SCENARIODEBUG.fields_by_name['scenario_type']._serialized_options = b'\x18\x01'
    _SCENARIODEBUG.fields_by_name['stage_type']._options = None
    _SCENARIODEBUG.fields_by_name['stage_type']._serialized_options = b'\x18\x01'
    _LANECHANGETYPE._serialized_start = 8185
    _LANECHANGETYPE._serialized_end = 8251
    _LANEBORROWTYPE._serialized_start = 8253
    _LANEBORROWTYPE._serialized_end = 8319
    _DEBUG._serialized_start = 745
    _DEBUG._serialized_end = 815
    _SPEEDPLAN._serialized_start = 817
    _SPEEDPLAN._serialized_end = 890
    _STGRAPHBOUNDARYDEBUG._serialized_start = 893
    _STGRAPHBOUNDARYDEBUG._serialized_end = 1283
    _STGRAPHBOUNDARYDEBUG_STBOUNDARYTYPE._serialized_start = 1051
    _STGRAPHBOUNDARYDEBUG_STBOUNDARYTYPE._serialized_end = 1283
    _SLFRAMEDEBUG._serialized_start = 1286
    _SLFRAMEDEBUG._serialized_end = 1672
    _STGRAPHDEBUG._serialized_start = 1675
    _STGRAPHDEBUG._serialized_end = 2333
    _STGRAPHDEBUG_STGRAPHSPEEDCONSTRAINT._serialized_start = 2137
    _STGRAPHDEBUG_STGRAPHSPEEDCONSTRAINT._serialized_end = 2214
    _STGRAPHDEBUG_STGRAPHKERNELCUISEREF._serialized_start = 2216
    _STGRAPHDEBUG_STGRAPHKERNELCUISEREF._serialized_end = 2273
    _STGRAPHDEBUG_STGRAPHKERNELFOLLOWREF._serialized_start = 2275
    _STGRAPHDEBUG_STGRAPHKERNELFOLLOWREF._serialized_end = 2333
    _SIGNALLIGHTDEBUG._serialized_start = 2336
    _SIGNALLIGHTDEBUG._serialized_end = 2637
    _SIGNALLIGHTDEBUG_SIGNALDEBUG._serialized_start = 2469
    _SIGNALLIGHTDEBUG_SIGNALDEBUG._serialized_end = 2637
    _DECISIONTAG._serialized_start = 2639
    _DECISIONTAG._serialized_end = 2728
    _OBSTACLEDEBUG._serialized_start = 2731
    _OBSTACLEDEBUG._serialized_end = 2923
    _REFERENCELINEDEBUG._serialized_start = 2926
    _REFERENCELINEDEBUG._serialized_end = 3271
    _SAMPLELAYERDEBUG._serialized_start = 3273
    _SAMPLELAYERDEBUG._serialized_end = 3333
    _DPPOLYGRAPHDEBUG._serialized_start = 3336
    _DPPOLYGRAPHDEBUG._serialized_end = 3468
    _SCENARIODEBUG._serialized_start = 3471
    _SCENARIODEBUG._serialized_end = 3607
    _TRAJECTORIES._serialized_start = 3609
    _TRAJECTORIES._serialized_end = 3670
    _OPENSPACEDEBUG._serialized_start = 3673
    _OPENSPACEDEBUG._serialized_end = 4654
    _SMOOTHERDEBUG._serialized_start = 4657
    _SMOOTHERDEBUG._serialized_end = 4852
    _SMOOTHERDEBUG_SMOOTHERTYPE._serialized_start = 4794
    _SMOOTHERDEBUG_SMOOTHERTYPE._serialized_end = 4852
    _PULLOVERDEBUG._serialized_start = 4855
    _PULLOVERDEBUG._serialized_end = 5012
    _PLANNINGDATA._serialized_start = 5015
    _PLANNINGDATA._serialized_end = 6410
    _LATTICESTPIXEL._serialized_start = 6412
    _LATTICESTPIXEL._serialized_end = 6483
    _LATTICESTTRAINING._serialized_start = 6486
    _LATTICESTTRAINING._serialized_end = 6687
    _COSTCOMPONENTS._serialized_start = 6689
    _COSTCOMPONENTS._serialized_end = 6729
    _AUTOTUNINGTRAININGDATA._serialized_start = 6732
    _AUTOTUNINGTRAININGDATA._serialized_end = 6894
    _CLOUDREFERENCELINEREQUEST._serialized_start = 6896
    _CLOUDREFERENCELINEREQUEST._serialized_end = 6974
    _CLOUDREFERENCELINEROUTINGREQUEST._serialized_start = 6976
    _CLOUDREFERENCELINEROUTINGREQUEST._serialized_end = 7060
    _CLOUDREFERENCELINERESPONSE._serialized_start = 7062
    _CLOUDREFERENCELINERESPONSE._serialized_end = 7128
    _HYBRIDMODELDEBUG._serialized_start = 7131
    _HYBRIDMODELDEBUG._serialized_end = 7334
    _NUDGEOBSTACLEDEBUG._serialized_start = 7337
    _NUDGEOBSTACLEDEBUG._serialized_end = 7566
    _NUDGEOBSTACLEDEBUG_NUDGETYPE._serialized_start = 7508
    _NUDGEOBSTACLEDEBUG_NUDGETYPE._serialized_end = 7566
    _LANETURNINFO._serialized_start = 7568
    _LANETURNINFO._serialized_end = 7664
    _ADCDRIVINGSTATE._serialized_start = 7667
    _ADCDRIVINGSTATE._serialized_end = 8183