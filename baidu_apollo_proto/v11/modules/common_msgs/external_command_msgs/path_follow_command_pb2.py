"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
_sym_db = _symbol_database.Default()
from ....modules.common_msgs.basic_msgs import header_pb2 as modules_dot_common__msgs_dot_basic__msgs_dot_header__pb2
from ....modules.common_msgs.external_command_msgs import geometry_pb2 as modules_dot_common__msgs_dot_external__command__msgs_dot_geometry__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\nCmodules/common_msgs/external_command_msgs/path_follow_command.proto\x12\x17apollo.external_command\x1a+modules/common_msgs/basic_msgs/header.proto\x1a8modules/common_msgs/external_command_msgs/geometry.proto"}\n\x0cPathBoundary\x125\n\rleft_boundary\x18\x01 \x03(\x0b2\x1e.apollo.external_command.Point\x126\n\x0eright_boundary\x18\x02 \x03(\x0b2\x1e.apollo.external_command.Point"F\n\x11BoundaryWithWidth\x12\x17\n\x0fleft_path_width\x18\x01 \x02(\x01\x12\x18\n\x10right_path_width\x18\x02 \x02(\x01"\xb2\x02\n\x11PathFollowCommand\x12%\n\x06header\x18\x01 \x01(\x0b2\x15.apollo.common.Header\x12\x16\n\ncommand_id\x18\x02 \x01(\x03:\x02-1\x121\n\tway_point\x18\x03 \x03(\x0b2\x1e.apollo.external_command.Point\x12>\n\rpath_boundary\x18\x04 \x01(\x0b2%.apollo.external_command.PathBoundaryH\x00\x12I\n\x13boundary_with_width\x18\x05 \x01(\x0b2*.apollo.external_command.BoundaryWithWidthH\x00\x12\x14\n\x0ctarget_speed\x18\x06 \x01(\x01B\n\n\x08boundary')
_PATHBOUNDARY = DESCRIPTOR.message_types_by_name['PathBoundary']
_BOUNDARYWITHWIDTH = DESCRIPTOR.message_types_by_name['BoundaryWithWidth']
_PATHFOLLOWCOMMAND = DESCRIPTOR.message_types_by_name['PathFollowCommand']
PathBoundary = _reflection.GeneratedProtocolMessageType('PathBoundary', (_message.Message,), {'DESCRIPTOR': _PATHBOUNDARY, '__module__': 'modules.common_msgs.external_command_msgs.path_follow_command_pb2'})
_sym_db.RegisterMessage(PathBoundary)
BoundaryWithWidth = _reflection.GeneratedProtocolMessageType('BoundaryWithWidth', (_message.Message,), {'DESCRIPTOR': _BOUNDARYWITHWIDTH, '__module__': 'modules.common_msgs.external_command_msgs.path_follow_command_pb2'})
_sym_db.RegisterMessage(BoundaryWithWidth)
PathFollowCommand = _reflection.GeneratedProtocolMessageType('PathFollowCommand', (_message.Message,), {'DESCRIPTOR': _PATHFOLLOWCOMMAND, '__module__': 'modules.common_msgs.external_command_msgs.path_follow_command_pb2'})
_sym_db.RegisterMessage(PathFollowCommand)
if _descriptor._USE_C_DESCRIPTORS == False:
    DESCRIPTOR._options = None
    _PATHBOUNDARY._serialized_start = 199
    _PATHBOUNDARY._serialized_end = 324
    _BOUNDARYWITHWIDTH._serialized_start = 326
    _BOUNDARYWITHWIDTH._serialized_end = 396
    _PATHFOLLOWCOMMAND._serialized_start = 399
    _PATHFOLLOWCOMMAND._serialized_end = 705