"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
_sym_db = _symbol_database.Default()
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n/modules/drivers/lidar/seyond/proto/seyond.proto\x12\x15apollo.drivers.seyond"@\n\x0cSeyondPacket\x12\x13\n\x0btable_exist\x18\x01 \x01(\x08\x12\x0c\n\x04data\x18\x02 \x01(\x0c\x12\r\n\x05table\x18\x03 \x01(\x0c"o\n\nSeyondScan\x12\x11\n\ttimestamp\x18\x01 \x01(\x04\x12\x18\n\x10measurement_time\x18\x02 \x01(\x01\x124\n\x07packets\x18\x03 \x03(\x0b2#.apollo.drivers.seyond.SeyondPacket')
_SEYONDPACKET = DESCRIPTOR.message_types_by_name['SeyondPacket']
_SEYONDSCAN = DESCRIPTOR.message_types_by_name['SeyondScan']
SeyondPacket = _reflection.GeneratedProtocolMessageType('SeyondPacket', (_message.Message,), {'DESCRIPTOR': _SEYONDPACKET, '__module__': 'modules.drivers.lidar.seyond.proto.seyond_pb2'})
_sym_db.RegisterMessage(SeyondPacket)
SeyondScan = _reflection.GeneratedProtocolMessageType('SeyondScan', (_message.Message,), {'DESCRIPTOR': _SEYONDSCAN, '__module__': 'modules.drivers.lidar.seyond.proto.seyond_pb2'})
_sym_db.RegisterMessage(SeyondScan)
if _descriptor._USE_C_DESCRIPTORS == False:
    DESCRIPTOR._options = None
    _SEYONDPACKET._serialized_start = 74
    _SEYONDPACKET._serialized_end = 138
    _SEYONDSCAN._serialized_start = 140
    _SEYONDSCAN._serialized_end = 251