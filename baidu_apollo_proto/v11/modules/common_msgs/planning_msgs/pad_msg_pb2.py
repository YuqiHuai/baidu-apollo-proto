"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
_sym_db = _symbol_database.Default()
from ....modules.common_msgs.basic_msgs import header_pb2 as modules_dot_common__msgs_dot_basic__msgs_dot_header__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n/modules/common_msgs/planning_msgs/pad_msg.proto\x12\x0fapollo.planning\x1a+modules/common_msgs/basic_msgs/header.proto"\x9e\x02\n\nPadMessage\x12%\n\x06header\x18\x01 \x01(\x0b2\x15.apollo.common.Header\x129\n\x06action\x18\x02 \x01(\x0e2).apollo.planning.PadMessage.DrivingAction"\xad\x01\n\rDrivingAction\x12\x08\n\x04NONE\x10d\x12\n\n\x06FOLLOW\x10\x00\x12\x0f\n\x0bCHANGE_LEFT\x10\x01\x12\x10\n\x0cCHANGE_RIGHT\x10\x02\x12\r\n\tPULL_OVER\x10\x03\x12\x08\n\x04STOP\x10\x04\x12\x11\n\rRESUME_CRUISE\x10\x05\x12\x12\n\x0eCLEAR_PLANNING\x10\x06\x12\x11\n\rENTER_MISSION\x10\x07\x12\x10\n\x0cEXIT_MISSION\x10\x08')
_PADMESSAGE = DESCRIPTOR.message_types_by_name['PadMessage']
_PADMESSAGE_DRIVINGACTION = _PADMESSAGE.enum_types_by_name['DrivingAction']
PadMessage = _reflection.GeneratedProtocolMessageType('PadMessage', (_message.Message,), {'DESCRIPTOR': _PADMESSAGE, '__module__': 'modules.common_msgs.planning_msgs.pad_msg_pb2'})
_sym_db.RegisterMessage(PadMessage)
if _descriptor._USE_C_DESCRIPTORS == False:
    DESCRIPTOR._options = None
    _PADMESSAGE._serialized_start = 114
    _PADMESSAGE._serialized_end = 400
    _PADMESSAGE_DRIVINGACTION._serialized_start = 227
    _PADMESSAGE_DRIVINGACTION._serialized_end = 400