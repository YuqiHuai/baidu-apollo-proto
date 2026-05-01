"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
_sym_db = _symbol_database.Default()
from ....modules.common_msgs.map_msgs import map_geometry_pb2 as modules_dot_common__msgs_dot_map__msgs_dot_map__geometry__pb2
from ....modules.common_msgs.map_msgs import map_id_pb2 as modules_dot_common__msgs_dot_map__msgs_dot_map__id__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n+modules/common_msgs/map_msgs/map_area.proto\x12\x0capollo.hdmap\x1a/modules/common_msgs/map_msgs/map_geometry.proto\x1a)modules/common_msgs/map_msgs/map_id.proto"\xf6\x01\n\x04Area\x12\x1c\n\x02id\x18\x01 \x02(\x0b2\x10.apollo.hdmap.Id\x12%\n\x04type\x18\x02 \x01(\x0e2\x17.apollo.hdmap.Area.Type\x12&\n\x07polygon\x18\x03 \x02(\x0b2\x15.apollo.hdmap.Polygon\x12$\n\noverlap_id\x18\x04 \x03(\x0b2\x10.apollo.hdmap.Id\x12\x0c\n\x04name\x18\x05 \x01(\t"M\n\x04Type\x12\r\n\tDriveable\x10\x01\x12\x0f\n\x0bUnDriveable\x10\x02\x12\x0b\n\x07Custom1\x10\x03\x12\x0b\n\x07Custom2\x10\x04\x12\x0b\n\x07Custom3\x10\x05')
_AREA = DESCRIPTOR.message_types_by_name['Area']
_AREA_TYPE = _AREA.enum_types_by_name['Type']
Area = _reflection.GeneratedProtocolMessageType('Area', (_message.Message,), {'DESCRIPTOR': _AREA, '__module__': 'modules.common_msgs.map_msgs.map_area_pb2'})
_sym_db.RegisterMessage(Area)
if _descriptor._USE_C_DESCRIPTORS == False:
    DESCRIPTOR._options = None
    _AREA._serialized_start = 154
    _AREA._serialized_end = 400
    _AREA_TYPE._serialized_start = 323
    _AREA_TYPE._serialized_end = 400