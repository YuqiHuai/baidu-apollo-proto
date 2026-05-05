"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
_sym_db = _symbol_database.Default()
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n/modules/dreamview_plus/proto/data_handler.proto\x12\x10apollo.dreamview"?\n\rWebsocketInfo\x12\x16\n\x0ewebsocket_name\x18\x01 \x01(\t\x12\x16\n\x0ewebsocket_pipe\x18\x02 \x01(\t"I\n\x0bChannelInfo\x12\x14\n\x0cchannel_name\x18\x01 \x01(\t\x12\x12\n\nproto_path\x18\x02 \x01(\t\x12\x10\n\x08msg_type\x18\x03 \x01(\t"\xdb\x01\n\x0fDataHandlerInfo\x12\x11\n\tdata_name\x18\x01 \x01(\t\x12\x12\n\nproto_path\x18\x02 \x01(\t\x12\x10\n\x08msg_type\x18\x03 \x01(\t\x127\n\x0ewebsocket_info\x18\x04 \x01(\x0b2\x1f.apollo.dreamview.WebsocketInfo\x12%\n\x16different_for_channels\x18\x05 \x01(\x08:\x05false\x12/\n\x08channels\x18\x06 \x03(\x0b2\x1d.apollo.dreamview.ChannelInfo"\xbf\x01\n\x0fDataHandlerConf\x12Q\n\x11data_handler_info\x18\x01 \x03(\x0b26.apollo.dreamview.DataHandlerConf.DataHandlerInfoEntry\x1aY\n\x14DataHandlerInfoEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x120\n\x05value\x18\x02 \x01(\x0b2!.apollo.dreamview.DataHandlerInfo:\x028\x01"a\n\nStreamData\x12\x0c\n\x04type\x18\x01 \x01(\t\x12\x0e\n\x06action\x18\x02 \x01(\t\x12\x11\n\tdata_name\x18\x03 \x01(\t\x12\x14\n\x0cchannel_name\x18\x04 \x01(\t\x12\x0c\n\x04data\x18\x05 \x01(\x0c')
_WEBSOCKETINFO = DESCRIPTOR.message_types_by_name['WebsocketInfo']
_CHANNELINFO = DESCRIPTOR.message_types_by_name['ChannelInfo']
_DATAHANDLERINFO = DESCRIPTOR.message_types_by_name['DataHandlerInfo']
_DATAHANDLERCONF = DESCRIPTOR.message_types_by_name['DataHandlerConf']
_DATAHANDLERCONF_DATAHANDLERINFOENTRY = _DATAHANDLERCONF.nested_types_by_name['DataHandlerInfoEntry']
_STREAMDATA = DESCRIPTOR.message_types_by_name['StreamData']
WebsocketInfo = _reflection.GeneratedProtocolMessageType('WebsocketInfo', (_message.Message,), {'DESCRIPTOR': _WEBSOCKETINFO, '__module__': 'modules.dreamview_plus.proto.data_handler_pb2'})
_sym_db.RegisterMessage(WebsocketInfo)
ChannelInfo = _reflection.GeneratedProtocolMessageType('ChannelInfo', (_message.Message,), {'DESCRIPTOR': _CHANNELINFO, '__module__': 'modules.dreamview_plus.proto.data_handler_pb2'})
_sym_db.RegisterMessage(ChannelInfo)
DataHandlerInfo = _reflection.GeneratedProtocolMessageType('DataHandlerInfo', (_message.Message,), {'DESCRIPTOR': _DATAHANDLERINFO, '__module__': 'modules.dreamview_plus.proto.data_handler_pb2'})
_sym_db.RegisterMessage(DataHandlerInfo)
DataHandlerConf = _reflection.GeneratedProtocolMessageType('DataHandlerConf', (_message.Message,), {'DataHandlerInfoEntry': _reflection.GeneratedProtocolMessageType('DataHandlerInfoEntry', (_message.Message,), {'DESCRIPTOR': _DATAHANDLERCONF_DATAHANDLERINFOENTRY, '__module__': 'modules.dreamview_plus.proto.data_handler_pb2'}), 'DESCRIPTOR': _DATAHANDLERCONF, '__module__': 'modules.dreamview_plus.proto.data_handler_pb2'})
_sym_db.RegisterMessage(DataHandlerConf)
_sym_db.RegisterMessage(DataHandlerConf.DataHandlerInfoEntry)
StreamData = _reflection.GeneratedProtocolMessageType('StreamData', (_message.Message,), {'DESCRIPTOR': _STREAMDATA, '__module__': 'modules.dreamview_plus.proto.data_handler_pb2'})
_sym_db.RegisterMessage(StreamData)
if _descriptor._USE_C_DESCRIPTORS == False:
    DESCRIPTOR._options = None
    _DATAHANDLERCONF_DATAHANDLERINFOENTRY._options = None
    _DATAHANDLERCONF_DATAHANDLERINFOENTRY._serialized_options = b'8\x01'
    _WEBSOCKETINFO._serialized_start = 69
    _WEBSOCKETINFO._serialized_end = 132
    _CHANNELINFO._serialized_start = 134
    _CHANNELINFO._serialized_end = 207
    _DATAHANDLERINFO._serialized_start = 210
    _DATAHANDLERINFO._serialized_end = 429
    _DATAHANDLERCONF._serialized_start = 432
    _DATAHANDLERCONF._serialized_end = 623
    _DATAHANDLERCONF_DATAHANDLERINFOENTRY._serialized_start = 534
    _DATAHANDLERCONF_DATAHANDLERINFOENTRY._serialized_end = 623
    _STREAMDATA._serialized_start = 625
    _STREAMDATA._serialized_end = 722