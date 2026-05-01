"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
_sym_db = _symbol_database.Default()
from ....modules.common_msgs.basic_msgs import header_pb2 as modules_dot_common__msgs_dot_basic__msgs_dot_header__pb2
from ....modules.common_msgs.external_command_msgs import geometry_pb2 as modules_dot_common__msgs_dot_external__command__msgs_dot_geometry__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\nBmodules/common_msgs/external_command_msgs/zone_cover_command.proto\x12\x17apollo.external_command\x1a+modules/common_msgs/basic_msgs/header.proto\x1a8modules/common_msgs/external_command_msgs/geometry.proto"\x9f\x02\n\x10ZoneCoverCommand\x12%\n\x06header\x18\x01 \x01(\x0b2\x15.apollo.common.Header\x12\x16\n\ncommand_id\x18\x02 \x01(\x03:\x02-1\x12 \n\x11is_start_pose_set\x18\x03 \x01(\x08:\x05false\x12\x1a\n\x12zone_cover_area_id\x18\x04 \x02(\t\x12\x14\n\x0ctarget_speed\x18\x05 \x01(\x01\x12=\n\x10non_drivable_roi\x18\x06 \x03(\x0b2#.apollo.external_command.RoiPolygon\x129\n\x0cdrivable_roi\x18\x07 \x01(\x0b2#.apollo.external_command.RoiPolygon')
_ZONECOVERCOMMAND = DESCRIPTOR.message_types_by_name['ZoneCoverCommand']
ZoneCoverCommand = _reflection.GeneratedProtocolMessageType('ZoneCoverCommand', (_message.Message,), {'DESCRIPTOR': _ZONECOVERCOMMAND, '__module__': 'modules.common_msgs.external_command_msgs.zone_cover_command_pb2'})
_sym_db.RegisterMessage(ZoneCoverCommand)
if _descriptor._USE_C_DESCRIPTORS == False:
    DESCRIPTOR._options = None
    _ZONECOVERCOMMAND._serialized_start = 199
    _ZONECOVERCOMMAND._serialized_end = 486