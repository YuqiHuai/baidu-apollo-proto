"""Generated protocol buffer code."""
from google.protobuf.internal import enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
_sym_db = _symbol_database.Default()
from ....modules.common_msgs.basic_msgs import geometry_pb2 as modules_dot_common__msgs_dot_basic__msgs_dot_geometry__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n/modules/common_msgs/routing_msgs/geometry.proto\x12\x0eapollo.routing\x1a-modules/common_msgs/basic_msgs/geometry.proto"]\n\x0cLaneWaypoint\x12\n\n\x02id\x18\x01 \x01(\t\x12\t\n\x01s\x18\x02 \x01(\x01\x12%\n\x04pose\x18\x03 \x01(\x0b2\x17.apollo.common.PointENU\x12\x0f\n\x07heading\x18\x04 \x01(\x01"9\n\x0bLaneSegment\x12\n\n\x02id\x18\x01 \x01(\t\x12\x0f\n\x07start_s\x18\x02 \x01(\x01\x12\r\n\x05end_s\x18\x03 \x01(\x01"\x1f\n\x0bMeasurement\x12\x10\n\x08distance\x18\x01 \x01(\x01"\x8c\x01\n\x07Passage\x12,\n\x07segment\x18\x01 \x03(\x0b2\x1b.apollo.routing.LaneSegment\x12\x10\n\x08can_exit\x18\x02 \x01(\x08\x12A\n\x10change_lane_type\x18\x03 \x01(\x0e2\x1e.apollo.routing.ChangeLaneType:\x07FORWARD"C\n\x0bRoadSegment\x12\n\n\x02id\x18\x01 \x01(\t\x12(\n\x07passage\x18\x02 \x03(\x0b2\x17.apollo.routing.Passage*H\n\x12DeadEndRoutingType\x12\x11\n\rROUTING_OTHER\x10\x00\x12\x0e\n\nROUTING_IN\x10\x01\x12\x0f\n\x0bROUTING_OUT\x10\x02*2\n\x0eChangeLaneType\x12\x0b\n\x07FORWARD\x10\x00\x12\x08\n\x04LEFT\x10\x01\x12\t\n\x05RIGHT\x10\x02')
_DEADENDROUTINGTYPE = DESCRIPTOR.enum_types_by_name['DeadEndRoutingType']
DeadEndRoutingType = enum_type_wrapper.EnumTypeWrapper(_DEADENDROUTINGTYPE)
_CHANGELANETYPE = DESCRIPTOR.enum_types_by_name['ChangeLaneType']
ChangeLaneType = enum_type_wrapper.EnumTypeWrapper(_CHANGELANETYPE)
ROUTING_OTHER = 0
ROUTING_IN = 1
ROUTING_OUT = 2
FORWARD = 0
LEFT = 1
RIGHT = 2
_LANEWAYPOINT = DESCRIPTOR.message_types_by_name['LaneWaypoint']
_LANESEGMENT = DESCRIPTOR.message_types_by_name['LaneSegment']
_MEASUREMENT = DESCRIPTOR.message_types_by_name['Measurement']
_PASSAGE = DESCRIPTOR.message_types_by_name['Passage']
_ROADSEGMENT = DESCRIPTOR.message_types_by_name['RoadSegment']
LaneWaypoint = _reflection.GeneratedProtocolMessageType('LaneWaypoint', (_message.Message,), {'DESCRIPTOR': _LANEWAYPOINT, '__module__': 'modules.common_msgs.routing_msgs.geometry_pb2'})
_sym_db.RegisterMessage(LaneWaypoint)
LaneSegment = _reflection.GeneratedProtocolMessageType('LaneSegment', (_message.Message,), {'DESCRIPTOR': _LANESEGMENT, '__module__': 'modules.common_msgs.routing_msgs.geometry_pb2'})
_sym_db.RegisterMessage(LaneSegment)
Measurement = _reflection.GeneratedProtocolMessageType('Measurement', (_message.Message,), {'DESCRIPTOR': _MEASUREMENT, '__module__': 'modules.common_msgs.routing_msgs.geometry_pb2'})
_sym_db.RegisterMessage(Measurement)
Passage = _reflection.GeneratedProtocolMessageType('Passage', (_message.Message,), {'DESCRIPTOR': _PASSAGE, '__module__': 'modules.common_msgs.routing_msgs.geometry_pb2'})
_sym_db.RegisterMessage(Passage)
RoadSegment = _reflection.GeneratedProtocolMessageType('RoadSegment', (_message.Message,), {'DESCRIPTOR': _ROADSEGMENT, '__module__': 'modules.common_msgs.routing_msgs.geometry_pb2'})
_sym_db.RegisterMessage(RoadSegment)
if _descriptor._USE_C_DESCRIPTORS == False:
    DESCRIPTOR._options = None
    _DEADENDROUTINGTYPE._serialized_start = 513
    _DEADENDROUTINGTYPE._serialized_end = 585
    _CHANGELANETYPE._serialized_start = 587
    _CHANGELANETYPE._serialized_end = 637
    _LANEWAYPOINT._serialized_start = 114
    _LANEWAYPOINT._serialized_end = 207
    _LANESEGMENT._serialized_start = 209
    _LANESEGMENT._serialized_end = 266
    _MEASUREMENT._serialized_start = 268
    _MEASUREMENT._serialized_end = 299
    _PASSAGE._serialized_start = 302
    _PASSAGE._serialized_end = 442
    _ROADSEGMENT._serialized_start = 444
    _ROADSEGMENT._serialized_end = 511