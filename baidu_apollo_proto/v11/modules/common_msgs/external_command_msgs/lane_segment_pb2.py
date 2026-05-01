"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
_sym_db = _symbol_database.Default()
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n<modules/common_msgs/external_command_msgs/lane_segment.proto\x12\x17apollo.external_command"9\n\x0bLaneSegment\x12\n\n\x02id\x18\x01 \x01(\t\x12\x0f\n\x07start_s\x18\x02 \x01(\x01\x12\r\n\x05end_s\x18\x03 \x01(\x01')
_LANESEGMENT = DESCRIPTOR.message_types_by_name['LaneSegment']
LaneSegment = _reflection.GeneratedProtocolMessageType('LaneSegment', (_message.Message,), {'DESCRIPTOR': _LANESEGMENT, '__module__': 'modules.common_msgs.external_command_msgs.lane_segment_pb2'})
_sym_db.RegisterMessage(LaneSegment)
if _descriptor._USE_C_DESCRIPTORS == False:
    DESCRIPTOR._options = None
    _LANESEGMENT._serialized_start = 89
    _LANESEGMENT._serialized_end = 146