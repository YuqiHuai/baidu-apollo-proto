"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
_sym_db = _symbol_database.Default()
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\nPmodules/planning/tasks/open_space_roi_decider/proto/open_space_roi_decider.proto\x12\x0fapollo.planning"\xa4\x07\n\x19OpenSpaceRoiDeciderConfig\x12D\n\x08roi_type\x18\x01 \x01(\x0e22.apollo.planning.OpenSpaceRoiDeciderConfig.RoiType\x12(\n\x1croi_longitudinal_range_start\x18\x02 \x01(\x01:\x0210\x12&\n\x1aroi_longitudinal_range_end\x18\x03 \x01(\x01:\x0210\x12\x1e\n\x13parking_start_range\x18\x04 \x01(\x01:\x017\x12\x1e\n\x0fparking_inwards\x18\x05 \x01(\x08:\x05false\x12#\n\x1benable_perception_obstacles\x18\x06 \x01(\x08\x12!\n\x14parking_depth_buffer\x18\x07 \x01(\x01:\x030.1\x12\'\n\x1aroi_line_segment_min_angle\x18\x08 \x01(\x01:\x030.3\x12"\n\x17roi_line_segment_length\x18\t \x01(\x01:\x011\x12,\n roi_line_segment_length_from_map\x18\n \x01(\x01:\x0210\x124\n&perception_obstacle_filtering_distance\x18\x0b \x01(\x01:\x041000\x12"\n\x1aperception_obstacle_buffer\x18\x0c \x01(\x01\x122\n\'curb_heading_tangent_change_upper_limit\x18\r \x01(\x01:\x011\x12\x1f\n\x13end_pose_s_distance\x18\x0e \x01(\x01:\x0210\x12\'\n\x1aparallel_park_end_x_buffer\x18\x0f \x01(\x01:\x030.2\x12 \n\x15extend_right_x_buffer\x18\x10 \x01(\x01:\x010\x12\x1f\n\x14extend_left_x_buffer\x18\x11 \x01(\x01:\x010\x12)\n\x1ause_road_boundary_from_map\x18\x12 \x01(\x08:\x05false\x125\n&expand_polygon_of_obstacle_by_distance\x18\x13 \x01(\x08:\x05false"o\n\x07RoiType\x12\x0f\n\x0bNOT_DEFINED\x10\x00\x12\x0b\n\x07PARKING\x10\x01\x12\r\n\tPULL_OVER\x10\x02\x12\x0f\n\x0bPARK_AND_GO\x10\x03\x12\x18\n\x14NARROW_STREET_U_TURN\x10\x04\x12\x0c\n\x08DEAD_END\x10\x05')
_OPENSPACEROIDECIDERCONFIG = DESCRIPTOR.message_types_by_name['OpenSpaceRoiDeciderConfig']
_OPENSPACEROIDECIDERCONFIG_ROITYPE = _OPENSPACEROIDECIDERCONFIG.enum_types_by_name['RoiType']
OpenSpaceRoiDeciderConfig = _reflection.GeneratedProtocolMessageType('OpenSpaceRoiDeciderConfig', (_message.Message,), {'DESCRIPTOR': _OPENSPACEROIDECIDERCONFIG, '__module__': 'modules.planning.tasks.open_space_roi_decider.proto.open_space_roi_decider_pb2'})
_sym_db.RegisterMessage(OpenSpaceRoiDeciderConfig)
if _descriptor._USE_C_DESCRIPTORS == False:
    DESCRIPTOR._options = None
    _OPENSPACEROIDECIDERCONFIG._serialized_start = 102
    _OPENSPACEROIDECIDERCONFIG._serialized_end = 1034
    _OPENSPACEROIDECIDERCONFIG_ROITYPE._serialized_start = 923
    _OPENSPACEROIDECIDERCONFIG_ROITYPE._serialized_end = 1034