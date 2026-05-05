"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
_sym_db = _symbol_database.Default()
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n:modules/planning/tasks/rss_decider/proto/rss_decider.proto\x12\x0fapollo.planning"e\n\x10RssDeciderConfig\x12"\n\x13enable_rss_fallback\x18\x01 \x01(\x08:\x05false\x12-\n\x1frss_max_front_obstacle_distance\x18\x02 \x01(\x01:\x043000')
_RSSDECIDERCONFIG = DESCRIPTOR.message_types_by_name['RssDeciderConfig']
RssDeciderConfig = _reflection.GeneratedProtocolMessageType('RssDeciderConfig', (_message.Message,), {'DESCRIPTOR': _RSSDECIDERCONFIG, '__module__': 'modules.planning.tasks.rss_decider.proto.rss_decider_pb2'})
_sym_db.RegisterMessage(RssDeciderConfig)
if _descriptor._USE_C_DESCRIPTORS == False:
    DESCRIPTOR._options = None
    _RSSDECIDERCONFIG._serialized_start = 79
    _RSSDECIDERCONFIG._serialized_end = 180