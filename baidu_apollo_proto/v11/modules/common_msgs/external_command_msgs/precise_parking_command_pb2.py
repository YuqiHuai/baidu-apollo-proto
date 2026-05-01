"""Generated protocol buffer code."""
from google.protobuf.internal import enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
_sym_db = _symbol_database.Default()
from ....modules.common_msgs.basic_msgs import header_pb2 as modules_dot_common__msgs_dot_basic__msgs_dot_header__pb2
from ....modules.common_msgs.external_command_msgs import geometry_pb2 as modules_dot_common__msgs_dot_external__command__msgs_dot_geometry__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\nGmodules/common_msgs/external_command_msgs/precise_parking_command.proto\x12\x17apollo.external_command\x1a+modules/common_msgs/basic_msgs/header.proto\x1a8modules/common_msgs/external_command_msgs/geometry.proto"\xa4\x02\n\x15PreciseParkingCommand\x12%\n\x06header\x18\x01 \x01(\x0b2\x15.apollo.common.Header\x12\x16\n\ncommand_id\x18\x02 \x01(\x03:\x02-1\x12 \n\x11is_start_pose_set\x18\x03 \x01(\x08:\x05false\x128\n\x11parking_spot_pose\x18\x04 \x02(\x0b2\x1d.apollo.external_command.Pose\x12\x17\n\x0fparking_inwards\x18\x05 \x02(\x08\x12A\n\x0cmission_type\x18\x06 \x02(\x0e2+.apollo.external_command.PreciseMissionType\x12\x14\n\x0ctarget_speed\x18\x07 \x01(\x01**\n\x12PreciseMissionType\x12\n\n\x06CHARGE\x10\x00\x12\x08\n\x04DUMP\x10\x01')
_PRECISEMISSIONTYPE = DESCRIPTOR.enum_types_by_name['PreciseMissionType']
PreciseMissionType = enum_type_wrapper.EnumTypeWrapper(_PRECISEMISSIONTYPE)
CHARGE = 0
DUMP = 1
_PRECISEPARKINGCOMMAND = DESCRIPTOR.message_types_by_name['PreciseParkingCommand']
PreciseParkingCommand = _reflection.GeneratedProtocolMessageType('PreciseParkingCommand', (_message.Message,), {'DESCRIPTOR': _PRECISEPARKINGCOMMAND, '__module__': 'modules.common_msgs.external_command_msgs.precise_parking_command_pb2'})
_sym_db.RegisterMessage(PreciseParkingCommand)
if _descriptor._USE_C_DESCRIPTORS == False:
    DESCRIPTOR._options = None
    _PRECISEMISSIONTYPE._serialized_start = 498
    _PRECISEMISSIONTYPE._serialized_end = 540
    _PRECISEPARKINGCOMMAND._serialized_start = 204
    _PRECISEPARKINGCOMMAND._serialized_end = 496