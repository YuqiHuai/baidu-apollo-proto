"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
_sym_db = _symbol_database.Default()
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\nFmodules/external_command/external_command_demo/proto/demo_config.proto\x12\x1capollo.external_command_demo"\x1d\n\x05Point\x12\t\n\x01x\x18\x01 \x01(\x01\x12\t\n\x01y\x18\x02 \x01(\x01"B\n\x0cDrivable_roi\x122\n\x05point\x18\x01 \x03(\x0b2#.apollo.external_command_demo.Point"E\n\x0fUn_drivable_roi\x122\n\x05point\x18\x01 \x03(\x0b2#.apollo.external_command_demo.Point"\xf4\x04\n\nDemoConfig\x12\x1a\n\x0fleft_path_width\x18\x01 \x01(\x01:\x012\x12\x1b\n\x10right_path_width\x18\x02 \x01(\x01:\x012\x12\x17\n\x0ctarget_speed\x18\x03 \x01(\x01:\x012\x12\x1d\n\x12min_distance_error\x18\x04 \x01(\x01:\x011\x12\x10\n\x08point1_x\x18\x05 \x01(\x01\x12\x10\n\x08point1_y\x18\x06 \x01(\x01\x12\x10\n\x08point2_x\x18\x07 \x01(\x01\x12\x10\n\x08point2_y\x18\x08 \x01(\x01\x12\x10\n\x08point3_x\x18\t \x01(\x01\x12\x10\n\x08point3_y\x18\n \x01(\x01\x12\x10\n\x08point4_x\x18\x0b \x01(\x01\x12\x10\n\x08point4_y\x18\x0c \x01(\x01\x12\x12\n\nend_pose_x\x18\r \x01(\x01\x12\x12\n\nend_pose_y\x18\x0e \x01(\x01\x12\x1b\n\x10end_pose_heading\x18\x0f \x01(\x01:\x010\x124\n,file_of_path_follow_with_localization_record\x18\x10 \x01(\t\x120\n(file_of_path_follow_with_planning_record\x18\x11 \x01(\t\x12@\n\x0cdrivable_roi\x18\x12 \x01(\x0b2*.apollo.external_command_demo.Drivable_roi\x12F\n\x0fun_drivable_roi\x18\x13 \x01(\x0b2-.apollo.external_command_demo.Un_drivable_roi\x12\x12\n\noverlap_id\x18\x14 \x01(\t\x12\x1a\n\x12zone_cover_area_id\x18\x15 \x01(\t')
_POINT = DESCRIPTOR.message_types_by_name['Point']
_DRIVABLE_ROI = DESCRIPTOR.message_types_by_name['Drivable_roi']
_UN_DRIVABLE_ROI = DESCRIPTOR.message_types_by_name['Un_drivable_roi']
_DEMOCONFIG = DESCRIPTOR.message_types_by_name['DemoConfig']
Point = _reflection.GeneratedProtocolMessageType('Point', (_message.Message,), {'DESCRIPTOR': _POINT, '__module__': 'modules.external_command.external_command_demo.proto.demo_config_pb2'})
_sym_db.RegisterMessage(Point)
Drivable_roi = _reflection.GeneratedProtocolMessageType('Drivable_roi', (_message.Message,), {'DESCRIPTOR': _DRIVABLE_ROI, '__module__': 'modules.external_command.external_command_demo.proto.demo_config_pb2'})
_sym_db.RegisterMessage(Drivable_roi)
Un_drivable_roi = _reflection.GeneratedProtocolMessageType('Un_drivable_roi', (_message.Message,), {'DESCRIPTOR': _UN_DRIVABLE_ROI, '__module__': 'modules.external_command.external_command_demo.proto.demo_config_pb2'})
_sym_db.RegisterMessage(Un_drivable_roi)
DemoConfig = _reflection.GeneratedProtocolMessageType('DemoConfig', (_message.Message,), {'DESCRIPTOR': _DEMOCONFIG, '__module__': 'modules.external_command.external_command_demo.proto.demo_config_pb2'})
_sym_db.RegisterMessage(DemoConfig)
if _descriptor._USE_C_DESCRIPTORS == False:
    DESCRIPTOR._options = None
    _POINT._serialized_start = 104
    _POINT._serialized_end = 133
    _DRIVABLE_ROI._serialized_start = 135
    _DRIVABLE_ROI._serialized_end = 201
    _UN_DRIVABLE_ROI._serialized_start = 203
    _UN_DRIVABLE_ROI._serialized_end = 272
    _DEMOCONFIG._serialized_start = 275
    _DEMOCONFIG._serialized_end = 903