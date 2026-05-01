"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
_sym_db = _symbol_database.Default()
from ....modules.common_msgs.basic_msgs import error_code_pb2 as modules_dot_common__msgs_dot_basic__msgs_dot_error__code__pb2
from ....modules.common_msgs.basic_msgs import geometry_pb2 as modules_dot_common__msgs_dot_basic__msgs_dot_geometry__pb2
from ....modules.common_msgs.basic_msgs import header_pb2 as modules_dot_common__msgs_dot_basic__msgs_dot_header__pb2
from ....modules.common_msgs.basic_msgs import pnc_point_pb2 as modules_dot_common__msgs_dot_basic__msgs_dot_pnc__point__pb2
from ....modules.common_msgs.map_msgs import map_lane_pb2 as modules_dot_common__msgs_dot_map__msgs_dot_map__lane__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n=modules/common_msgs/perception_msgs/perception_obstacle.proto\x12\x11apollo.perception\x1a/modules/common_msgs/basic_msgs/error_code.proto\x1a-modules/common_msgs/basic_msgs/geometry.proto\x1a+modules/common_msgs/basic_msgs/header.proto\x1a.modules/common_msgs/basic_msgs/pnc_point.proto\x1a+modules/common_msgs/map_msgs/map_lane.proto"@\n\x06BBox2D\x12\x0c\n\x04xmin\x18\x01 \x01(\x01\x12\x0c\n\x04ymin\x18\x02 \x01(\x01\x12\x0c\n\x04xmax\x18\x03 \x01(\x01\x12\x0c\n\x04ymax\x18\x04 \x01(\x01"\xaf\x01\n\x0bLightStatus\x12\x15\n\rbrake_visible\x18\x01 \x01(\x01\x12\x17\n\x0fbrake_switch_on\x18\x02 \x01(\x01\x12\x19\n\x11left_turn_visible\x18\x03 \x01(\x01\x12\x1b\n\x13left_turn_switch_on\x18\x04 \x01(\x01\x12\x1a\n\x12right_turn_visible\x18\x05 \x01(\x01\x12\x1c\n\x14right_turn_switch_on\x18\x06 \x01(\x01"\x83\x01\n\x0eV2XInformation\x12;\n\x08v2x_type\x18\x01 \x03(\x0e2).apollo.perception.V2XInformation.V2XType"4\n\x07V2XType\x12\x08\n\x04NONE\x10\x00\x12\x0f\n\x0bZOMBIES_CAR\x10\x01\x12\x0e\n\nBLIND_ZONE\x10\x02"\xfa\x02\n\x11SensorMeasurement\x12\x11\n\tsensor_id\x18\x01 \x01(\t\x12\n\n\x02id\x18\x02 \x01(\x05\x12(\n\x08position\x18\x03 \x01(\x0b2\x16.apollo.common.Point3D\x12\r\n\x05theta\x18\x04 \x01(\x01\x12\x0e\n\x06length\x18\x05 \x01(\x01\x12\r\n\x05width\x18\x06 \x01(\x01\x12\x0e\n\x06height\x18\x07 \x01(\x01\x12(\n\x08velocity\x18\x08 \x01(\x0b2\x16.apollo.common.Point3D\x128\n\x04type\x18\t \x01(\x0e2*.apollo.perception.PerceptionObstacle.Type\x12?\n\x08sub_type\x18\n \x01(\x0e2-.apollo.perception.PerceptionObstacle.SubType\x12\x11\n\ttimestamp\x18\x0b \x01(\x01\x12&\n\x03box\x18\x0c \x01(\x0b2\x19.apollo.perception.BBox2D"[\n\nTrajectory\x12\x13\n\x0bprobability\x18\x01 \x01(\x01\x128\n\x10trajectory_point\x18\x02 \x03(\x0b2\x1e.apollo.common.TrajectoryPoint"A\n\x0cDebugMessage\x121\n\ntrajectory\x18\x01 \x03(\x0b2\x1d.apollo.perception.Trajectory"\xff\x0f\n\x12PerceptionObstacle\x12\n\n\x02id\x18\x01 \x01(\x05\x12(\n\x08position\x18\x02 \x01(\x0b2\x16.apollo.common.Point3D\x12\r\n\x05theta\x18\x03 \x01(\x01\x12(\n\x08velocity\x18\x04 \x01(\x0b2\x16.apollo.common.Point3D\x12\x0e\n\x06length\x18\x05 \x01(\x01\x12\r\n\x05width\x18\x06 \x01(\x01\x12\x0e\n\x06height\x18\x07 \x01(\x01\x12-\n\rpolygon_point\x18\x08 \x03(\x0b2\x16.apollo.common.Point3D\x12\x15\n\rtracking_time\x18\t \x01(\x01\x128\n\x04type\x18\n \x01(\x0e2*.apollo.perception.PerceptionObstacle.Type\x12\x11\n\ttimestamp\x18\x0b \x01(\x01\x12\x17\n\x0bpoint_cloud\x18\x0c \x03(\x01B\x02\x10\x01\x12\x12\n\nconfidence\x18\r \x01(\x01\x12Q\n\x0fconfidence_type\x18\x0e \x01(\x0e24.apollo.perception.PerceptionObstacle.ConfidenceTypeB\x02\x18\x01\x12)\n\x05drops\x18\x0f \x03(\x0b2\x16.apollo.common.Point3DB\x02\x18\x01\x12,\n\x0cacceleration\x18\x10 \x01(\x0b2\x16.apollo.common.Point3D\x12,\n\x0canchor_point\x18\x11 \x01(\x0b2\x16.apollo.common.Point3D\x12)\n\x06bbox2d\x18\x12 \x01(\x0b2\x19.apollo.perception.BBox2D\x12?\n\x08sub_type\x18\x13 \x01(\x0e2-.apollo.perception.PerceptionObstacle.SubType\x12:\n\x0cmeasurements\x18\x14 \x03(\x0b2$.apollo.perception.SensorMeasurement\x12 \n\x13height_above_ground\x18\x15 \x01(\x01:\x03nan\x12\x1f\n\x13position_covariance\x18\x16 \x03(\x01B\x02\x10\x01\x12\x1f\n\x13velocity_covariance\x18\x17 \x03(\x01B\x02\x10\x01\x12#\n\x17acceleration_covariance\x18\x18 \x03(\x01B\x02\x10\x01\x124\n\x0clight_status\x18\x19 \x01(\x0b2\x1e.apollo.perception.LightStatus\x12,\n\x03msg\x18\x1a \x01(\x0b2\x1f.apollo.perception.DebugMessage\x12J\n\x06source\x18\x1b \x01(\x0e2,.apollo.perception.PerceptionObstacle.Source:\x0cHOST_VEHICLE\x123\n\x08v2x_info\x18\x1c \x01(\x0b2!.apollo.perception.V2XInformation\x12I\n\rsemantic_type\x18\x1d \x01(\x0e22.apollo.perception.PerceptionObstacle.SemanticType\x12E\n\x0bmotion_type\x18\x1e \x01(\x0e20.apollo.perception.PerceptionObstacle.MotionType"i\n\x04Type\x12\x0b\n\x07UNKNOWN\x10\x00\x12\x13\n\x0fUNKNOWN_MOVABLE\x10\x01\x12\x15\n\x11UNKNOWN_UNMOVABLE\x10\x02\x12\x0e\n\nPEDESTRIAN\x10\x03\x12\x0b\n\x07BICYCLE\x10\x04\x12\x0b\n\x07VEHICLE\x10\x05"R\n\x0eConfidenceType\x12\x16\n\x12CONFIDENCE_UNKNOWN\x10\x00\x12\x12\n\x0eCONFIDENCE_CNN\x10\x01\x12\x14\n\x10CONFIDENCE_RADAR\x10\x02"\x8b\x02\n\x07SubType\x12\x0e\n\nST_UNKNOWN\x10\x00\x12\x16\n\x12ST_UNKNOWN_MOVABLE\x10\x01\x12\x18\n\x14ST_UNKNOWN_UNMOVABLE\x10\x02\x12\n\n\x06ST_CAR\x10\x03\x12\n\n\x06ST_VAN\x10\x04\x12\x0c\n\x08ST_TRUCK\x10\x05\x12\n\n\x06ST_BUS\x10\x06\x12\x0e\n\nST_CYCLIST\x10\x07\x12\x13\n\x0fST_MOTORCYCLIST\x10\x08\x12\x11\n\rST_TRICYCLIST\x10\t\x12\x11\n\rST_PEDESTRIAN\x10\n\x12\x12\n\x0eST_TRAFFICCONE\x10\x0b\x12\x0f\n\x0bST_SMALLMOT\x10\x0c\x12\r\n\tST_BIGMOT\x10\r\x12\r\n\tST_NONMOT\x10\x0e"#\n\x06Source\x12\x10\n\x0cHOST_VEHICLE\x10\x00\x12\x07\n\x03V2X\x10\x01"\xb6\x01\n\x0cSemanticType\x12\x0e\n\nSM_UNKNOWN\x10\x00\x12\r\n\tSM_IGNORE\x10\x01\x12\r\n\tSM_GROUND\x10\x02\x12\r\n\tSM_OBJECT\x10\x03\x12\x0b\n\x07SM_CURB\x10\x04\x12\x11\n\rSM_VEGETATION\x10\x05\x12\x0c\n\x08SM_FENCE\x10\x06\x12\x0c\n\x08SM_NOISE\x10\x07\x12\x0b\n\x07SM_WALL\x10\x08\x12 \n\x1cSM_MAX_OBJECT_SEMANTIC_LABEL\x10\t"^\n\nMotionType\x12\x0e\n\nMT_UNKNOWN\x10\x00\x12\r\n\tMT_MOVING\x10\x01\x12\x11\n\rMT_STATIONARY\x10\x02\x12\x1e\n\x1aMT_MAX_OBJECT_MOTION_LABEL\x10\x03"\x95\x02\n\nLaneMarker\x126\n\tlane_type\x18\x01 \x01(\x0e2#.apollo.hdmap.LaneBoundaryType.Type\x12\x0f\n\x07quality\x18\x02 \x01(\x01\x12\x14\n\x0cmodel_degree\x18\x03 \x01(\x05\x12\x13\n\x0bc0_position\x18\x04 \x01(\x01\x12\x18\n\x10c1_heading_angle\x18\x05 \x01(\x01\x12\x14\n\x0cc2_curvature\x18\x06 \x01(\x01\x12\x1f\n\x17c3_curvature_derivative\x18\x07 \x01(\x01\x12\x12\n\nview_range\x18\x08 \x01(\x01\x12\x17\n\x0flongitude_start\x18\t \x01(\x01\x12\x15\n\rlongitude_end\x18\n \x01(\x01"\xfd\x01\n\x0bLaneMarkers\x127\n\x10left_lane_marker\x18\x01 \x01(\x0b2\x1d.apollo.perception.LaneMarker\x128\n\x11right_lane_marker\x18\x02 \x01(\x0b2\x1d.apollo.perception.LaneMarker\x12<\n\x15next_left_lane_marker\x18\x03 \x03(\x0b2\x1d.apollo.perception.LaneMarker\x12=\n\x16next_right_lane_marker\x18\x04 \x03(\x0b2\x1d.apollo.perception.LaneMarker"6\n\x08CIPVInfo\x12\x0f\n\x07cipv_id\x18\x01 \x01(\x05\x12\x19\n\x11potential_cipv_id\x18\x02 \x03(\x05"\xdb\x04\n\x0fPerceptionWaste\x12\n\n\x02id\x18\x01 \x01(\x05\x12(\n\x08position\x18\x02 \x01(\x0b2\x16.apollo.common.Point3D\x12\r\n\x05theta\x18\x03 \x01(\x01\x12(\n\x08velocity\x18\x04 \x01(\x0b2\x16.apollo.common.Point3D\x12\x0e\n\x06length\x18\x05 \x01(\x01\x12\r\n\x05width\x18\x06 \x01(\x01\x12\x0e\n\x06height\x18\x07 \x01(\x01\x12-\n\rpolygon_point\x18\x08 \x03(\x0b2\x16.apollo.common.Point3D\x12\x15\n\rtracking_time\x18\t \x01(\x01\x125\n\x04type\x18\n \x01(\x0e2\'.apollo.perception.PerceptionWaste.Type\x12\x11\n\ttimestamp\x18\x0b \x01(\x01\x12\x12\n\nconfidence\x18\x0c \x01(\x01\x12)\n\x06bbox2d\x18\r \x01(\x0b2\x19.apollo.perception.BBox2D\x12,\n\x03msg\x18\x0e \x01(\x0b2\x1f.apollo.perception.DebugMessage"\xac\x01\n\x04Type\x12\x0b\n\x07UNKNOWN\x10\x00\x12\x07\n\x03CAN\x10\x01\x12\r\n\tCIGARETTE\x10\x02\x12\x12\n\x0eCIGARETTE_CASE\x10\x03\x12\x08\n\x04PEEL\x10\x04\x12\x0b\n\x07PACKAGE\x10\x05\x12\x0f\n\x0bPLASTIC_BAG\x10\x06\x12\x0b\n\x07BOTTLES\x10\x07\x12\t\n\x05SHELL\x10\x08\x12\x08\n\x04LEAF\x10\t\x12\r\n\tPAPER_CUP\x10\n\x12\x08\n\x04CUBE\x10\x0b\x12\x08\n\x04WIRE\x10\x0c"\xd5\x02\n\x13PerceptionObstacles\x12B\n\x13perception_obstacle\x18\x01 \x03(\x0b2%.apollo.perception.PerceptionObstacle\x12%\n\x06header\x18\x02 \x01(\x0b2\x15.apollo.common.Header\x120\n\nerror_code\x18\x03 \x01(\x0e2\x18.apollo.common.ErrorCode:\x02OK\x123\n\x0blane_marker\x18\x04 \x01(\x0b2\x1e.apollo.perception.LaneMarkers\x12.\n\tcipv_info\x18\x05 \x01(\x0b2\x1b.apollo.perception.CIPVInfo\x12<\n\x10perception_waste\x18\x06 \x03(\x0b2".apollo.perception.PerceptionWaste"\xa9\x02\n\x12PerceptionEdgeInfo\x12%\n\x06header\x18\x01 \x01(\x0b2\x15.apollo.common.Header\x12\x19\n\nis_useable\x18\x02 \x01(\x08:\x05false\x12*\n\nedge_point\x18\x03 \x03(\x0b2\x16.apollo.common.Point3D\x123\n\x13edge_relative_point\x18\x04 \x03(\x0b2\x16.apollo.common.Point3D\x12\x14\n\x07delta_s\x18\x05 \x01(\x01:\x030.2\x12\x13\n\x0bedge_length\x18\x06 \x01(\x01\x12\x1f\n\x10is_smoother_succ\x18\x07 \x01(\x08:\x05false\x12$\n\x15is_cross_localization\x18\x08 \x01(\x08:\x05false"\xe3\x01\n\x1aPerceptionAccurateDockInfo\x12%\n\x06header\x18\x01 \x01(\x0b2\x15.apollo.common.Header\x12\x19\n\nis_useable\x18\x02 \x01(\x08:\x05false\x121\n\x11relative_position\x18\x03 \x01(\x0b2\x16.apollo.common.Point3D\x126\n\x16relative_path_position\x18\x04 \x03(\x0b2\x16.apollo.common.Point3D\x12\x18\n\x10relative_heading\x18\x05 \x01(\x01')
_BBOX2D = DESCRIPTOR.message_types_by_name['BBox2D']
_LIGHTSTATUS = DESCRIPTOR.message_types_by_name['LightStatus']
_V2XINFORMATION = DESCRIPTOR.message_types_by_name['V2XInformation']
_SENSORMEASUREMENT = DESCRIPTOR.message_types_by_name['SensorMeasurement']
_TRAJECTORY = DESCRIPTOR.message_types_by_name['Trajectory']
_DEBUGMESSAGE = DESCRIPTOR.message_types_by_name['DebugMessage']
_PERCEPTIONOBSTACLE = DESCRIPTOR.message_types_by_name['PerceptionObstacle']
_LANEMARKER = DESCRIPTOR.message_types_by_name['LaneMarker']
_LANEMARKERS = DESCRIPTOR.message_types_by_name['LaneMarkers']
_CIPVINFO = DESCRIPTOR.message_types_by_name['CIPVInfo']
_PERCEPTIONWASTE = DESCRIPTOR.message_types_by_name['PerceptionWaste']
_PERCEPTIONOBSTACLES = DESCRIPTOR.message_types_by_name['PerceptionObstacles']
_PERCEPTIONEDGEINFO = DESCRIPTOR.message_types_by_name['PerceptionEdgeInfo']
_PERCEPTIONACCURATEDOCKINFO = DESCRIPTOR.message_types_by_name['PerceptionAccurateDockInfo']
_V2XINFORMATION_V2XTYPE = _V2XINFORMATION.enum_types_by_name['V2XType']
_PERCEPTIONOBSTACLE_TYPE = _PERCEPTIONOBSTACLE.enum_types_by_name['Type']
_PERCEPTIONOBSTACLE_CONFIDENCETYPE = _PERCEPTIONOBSTACLE.enum_types_by_name['ConfidenceType']
_PERCEPTIONOBSTACLE_SUBTYPE = _PERCEPTIONOBSTACLE.enum_types_by_name['SubType']
_PERCEPTIONOBSTACLE_SOURCE = _PERCEPTIONOBSTACLE.enum_types_by_name['Source']
_PERCEPTIONOBSTACLE_SEMANTICTYPE = _PERCEPTIONOBSTACLE.enum_types_by_name['SemanticType']
_PERCEPTIONOBSTACLE_MOTIONTYPE = _PERCEPTIONOBSTACLE.enum_types_by_name['MotionType']
_PERCEPTIONWASTE_TYPE = _PERCEPTIONWASTE.enum_types_by_name['Type']
BBox2D = _reflection.GeneratedProtocolMessageType('BBox2D', (_message.Message,), {'DESCRIPTOR': _BBOX2D, '__module__': 'modules.common_msgs.perception_msgs.perception_obstacle_pb2'})
_sym_db.RegisterMessage(BBox2D)
LightStatus = _reflection.GeneratedProtocolMessageType('LightStatus', (_message.Message,), {'DESCRIPTOR': _LIGHTSTATUS, '__module__': 'modules.common_msgs.perception_msgs.perception_obstacle_pb2'})
_sym_db.RegisterMessage(LightStatus)
V2XInformation = _reflection.GeneratedProtocolMessageType('V2XInformation', (_message.Message,), {'DESCRIPTOR': _V2XINFORMATION, '__module__': 'modules.common_msgs.perception_msgs.perception_obstacle_pb2'})
_sym_db.RegisterMessage(V2XInformation)
SensorMeasurement = _reflection.GeneratedProtocolMessageType('SensorMeasurement', (_message.Message,), {'DESCRIPTOR': _SENSORMEASUREMENT, '__module__': 'modules.common_msgs.perception_msgs.perception_obstacle_pb2'})
_sym_db.RegisterMessage(SensorMeasurement)
Trajectory = _reflection.GeneratedProtocolMessageType('Trajectory', (_message.Message,), {'DESCRIPTOR': _TRAJECTORY, '__module__': 'modules.common_msgs.perception_msgs.perception_obstacle_pb2'})
_sym_db.RegisterMessage(Trajectory)
DebugMessage = _reflection.GeneratedProtocolMessageType('DebugMessage', (_message.Message,), {'DESCRIPTOR': _DEBUGMESSAGE, '__module__': 'modules.common_msgs.perception_msgs.perception_obstacle_pb2'})
_sym_db.RegisterMessage(DebugMessage)
PerceptionObstacle = _reflection.GeneratedProtocolMessageType('PerceptionObstacle', (_message.Message,), {'DESCRIPTOR': _PERCEPTIONOBSTACLE, '__module__': 'modules.common_msgs.perception_msgs.perception_obstacle_pb2'})
_sym_db.RegisterMessage(PerceptionObstacle)
LaneMarker = _reflection.GeneratedProtocolMessageType('LaneMarker', (_message.Message,), {'DESCRIPTOR': _LANEMARKER, '__module__': 'modules.common_msgs.perception_msgs.perception_obstacle_pb2'})
_sym_db.RegisterMessage(LaneMarker)
LaneMarkers = _reflection.GeneratedProtocolMessageType('LaneMarkers', (_message.Message,), {'DESCRIPTOR': _LANEMARKERS, '__module__': 'modules.common_msgs.perception_msgs.perception_obstacle_pb2'})
_sym_db.RegisterMessage(LaneMarkers)
CIPVInfo = _reflection.GeneratedProtocolMessageType('CIPVInfo', (_message.Message,), {'DESCRIPTOR': _CIPVINFO, '__module__': 'modules.common_msgs.perception_msgs.perception_obstacle_pb2'})
_sym_db.RegisterMessage(CIPVInfo)
PerceptionWaste = _reflection.GeneratedProtocolMessageType('PerceptionWaste', (_message.Message,), {'DESCRIPTOR': _PERCEPTIONWASTE, '__module__': 'modules.common_msgs.perception_msgs.perception_obstacle_pb2'})
_sym_db.RegisterMessage(PerceptionWaste)
PerceptionObstacles = _reflection.GeneratedProtocolMessageType('PerceptionObstacles', (_message.Message,), {'DESCRIPTOR': _PERCEPTIONOBSTACLES, '__module__': 'modules.common_msgs.perception_msgs.perception_obstacle_pb2'})
_sym_db.RegisterMessage(PerceptionObstacles)
PerceptionEdgeInfo = _reflection.GeneratedProtocolMessageType('PerceptionEdgeInfo', (_message.Message,), {'DESCRIPTOR': _PERCEPTIONEDGEINFO, '__module__': 'modules.common_msgs.perception_msgs.perception_obstacle_pb2'})
_sym_db.RegisterMessage(PerceptionEdgeInfo)
PerceptionAccurateDockInfo = _reflection.GeneratedProtocolMessageType('PerceptionAccurateDockInfo', (_message.Message,), {'DESCRIPTOR': _PERCEPTIONACCURATEDOCKINFO, '__module__': 'modules.common_msgs.perception_msgs.perception_obstacle_pb2'})
_sym_db.RegisterMessage(PerceptionAccurateDockInfo)
if _descriptor._USE_C_DESCRIPTORS == False:
    DESCRIPTOR._options = None
    _PERCEPTIONOBSTACLE.fields_by_name['point_cloud']._options = None
    _PERCEPTIONOBSTACLE.fields_by_name['point_cloud']._serialized_options = b'\x10\x01'
    _PERCEPTIONOBSTACLE.fields_by_name['confidence_type']._options = None
    _PERCEPTIONOBSTACLE.fields_by_name['confidence_type']._serialized_options = b'\x18\x01'
    _PERCEPTIONOBSTACLE.fields_by_name['drops']._options = None
    _PERCEPTIONOBSTACLE.fields_by_name['drops']._serialized_options = b'\x18\x01'
    _PERCEPTIONOBSTACLE.fields_by_name['position_covariance']._options = None
    _PERCEPTIONOBSTACLE.fields_by_name['position_covariance']._serialized_options = b'\x10\x01'
    _PERCEPTIONOBSTACLE.fields_by_name['velocity_covariance']._options = None
    _PERCEPTIONOBSTACLE.fields_by_name['velocity_covariance']._serialized_options = b'\x10\x01'
    _PERCEPTIONOBSTACLE.fields_by_name['acceleration_covariance']._options = None
    _PERCEPTIONOBSTACLE.fields_by_name['acceleration_covariance']._serialized_options = b'\x10\x01'
    _BBOX2D._serialized_start = 318
    _BBOX2D._serialized_end = 382
    _LIGHTSTATUS._serialized_start = 385
    _LIGHTSTATUS._serialized_end = 560
    _V2XINFORMATION._serialized_start = 563
    _V2XINFORMATION._serialized_end = 694
    _V2XINFORMATION_V2XTYPE._serialized_start = 642
    _V2XINFORMATION_V2XTYPE._serialized_end = 694
    _SENSORMEASUREMENT._serialized_start = 697
    _SENSORMEASUREMENT._serialized_end = 1075
    _TRAJECTORY._serialized_start = 1077
    _TRAJECTORY._serialized_end = 1168
    _DEBUGMESSAGE._serialized_start = 1170
    _DEBUGMESSAGE._serialized_end = 1235
    _PERCEPTIONOBSTACLE._serialized_start = 1238
    _PERCEPTIONOBSTACLE._serialized_end = 3285
    _PERCEPTIONOBSTACLE_TYPE._serialized_start = 2508
    _PERCEPTIONOBSTACLE_TYPE._serialized_end = 2613
    _PERCEPTIONOBSTACLE_CONFIDENCETYPE._serialized_start = 2615
    _PERCEPTIONOBSTACLE_CONFIDENCETYPE._serialized_end = 2697
    _PERCEPTIONOBSTACLE_SUBTYPE._serialized_start = 2700
    _PERCEPTIONOBSTACLE_SUBTYPE._serialized_end = 2967
    _PERCEPTIONOBSTACLE_SOURCE._serialized_start = 2969
    _PERCEPTIONOBSTACLE_SOURCE._serialized_end = 3004
    _PERCEPTIONOBSTACLE_SEMANTICTYPE._serialized_start = 3007
    _PERCEPTIONOBSTACLE_SEMANTICTYPE._serialized_end = 3189
    _PERCEPTIONOBSTACLE_MOTIONTYPE._serialized_start = 3191
    _PERCEPTIONOBSTACLE_MOTIONTYPE._serialized_end = 3285
    _LANEMARKER._serialized_start = 3288
    _LANEMARKER._serialized_end = 3565
    _LANEMARKERS._serialized_start = 3568
    _LANEMARKERS._serialized_end = 3821
    _CIPVINFO._serialized_start = 3823
    _CIPVINFO._serialized_end = 3877
    _PERCEPTIONWASTE._serialized_start = 3880
    _PERCEPTIONWASTE._serialized_end = 4483
    _PERCEPTIONWASTE_TYPE._serialized_start = 4311
    _PERCEPTIONWASTE_TYPE._serialized_end = 4483
    _PERCEPTIONOBSTACLES._serialized_start = 4486
    _PERCEPTIONOBSTACLES._serialized_end = 4827
    _PERCEPTIONEDGEINFO._serialized_start = 4830
    _PERCEPTIONEDGEINFO._serialized_end = 5127
    _PERCEPTIONACCURATEDOCKINFO._serialized_start = 5130
    _PERCEPTIONACCURATEDOCKINFO._serialized_end = 5357