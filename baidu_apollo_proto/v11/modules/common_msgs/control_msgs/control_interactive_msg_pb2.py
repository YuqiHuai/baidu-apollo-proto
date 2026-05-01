"""Generated protocol buffer code."""
from google.protobuf.internal import enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
_sym_db = _symbol_database.Default()
from ....modules.common_msgs.basic_msgs import header_pb2 as modules_dot_common__msgs_dot_basic__msgs_dot_header__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n>modules/common_msgs/control_msgs/control_interactive_msg.proto\x12\x0eapollo.control\x1a+modules/common_msgs/basic_msgs/header.proto"\xdc\x01\n\x15ControlInteractiveMsg\x12%\n\x06header\x18\x01 \x01(\x0b2\x15.apollo.common.Header\x12\x16\n\x0ereplan_request\x18\x02 \x01(\x08\x12G\n\x16replan_req_reason_code\x18\x03 \x01(\x0e2\'.apollo.control.ReplanRequestReasonCode\x12\x1d\n\x15replan_request_reason\x18\x04 \x01(\t\x12\x1c\n\x14is_need_safety_check\x18\x05 \x01(\x08*\x81\x01\n\x17ReplanRequestReasonCode\x12\x19\n\x15REPLAN_REQ_ALL_REPLAN\x10\x01\x12\x1d\n\x19REPLAN_REQ_STATION_REPLAN\x10\x02\x12\x1b\n\x17REPLAN_REQ_SPEED_REPLAN\x10\x03\x12\x0f\n\x0bNONE_REPLAN\x10\x04')
_REPLANREQUESTREASONCODE = DESCRIPTOR.enum_types_by_name['ReplanRequestReasonCode']
ReplanRequestReasonCode = enum_type_wrapper.EnumTypeWrapper(_REPLANREQUESTREASONCODE)
REPLAN_REQ_ALL_REPLAN = 1
REPLAN_REQ_STATION_REPLAN = 2
REPLAN_REQ_SPEED_REPLAN = 3
NONE_REPLAN = 4
_CONTROLINTERACTIVEMSG = DESCRIPTOR.message_types_by_name['ControlInteractiveMsg']
ControlInteractiveMsg = _reflection.GeneratedProtocolMessageType('ControlInteractiveMsg', (_message.Message,), {'DESCRIPTOR': _CONTROLINTERACTIVEMSG, '__module__': 'modules.common_msgs.control_msgs.control_interactive_msg_pb2'})
_sym_db.RegisterMessage(ControlInteractiveMsg)
if _descriptor._USE_C_DESCRIPTORS == False:
    DESCRIPTOR._options = None
    _REPLANREQUESTREASONCODE._serialized_start = 351
    _REPLANREQUESTREASONCODE._serialized_end = 480
    _CONTROLINTERACTIVEMSG._serialized_start = 128
    _CONTROLINTERACTIVEMSG._serialized_end = 348