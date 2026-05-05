"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
_sym_db = _symbol_database.Default()
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\nZmodules/planning/tasks/open_space_pre_stop_decider/proto/open_space_pre_stop_decider.proto\x12\x0fapollo.planning"\x8e\x02\n\x1dOpenSpacePreStopDeciderConfig\x12J\n\tstop_type\x18\x01 \x01(\x0e27.apollo.planning.OpenSpacePreStopDeciderConfig.StopType\x12"\n\x17rightaway_stop_distance\x18\x02 \x01(\x01:\x012\x12"\n\x17stop_distance_to_target\x18\x03 \x01(\x01:\x015\x12 \n\x15stop_buffer_to_target\x18\x04 \x01(\x01:\x010"7\n\x08StopType\x12\x0f\n\x0bNOT_DEFINED\x10\x00\x12\x0b\n\x07PARKING\x10\x01\x12\r\n\tPULL_OVER\x10\x02')
_OPENSPACEPRESTOPDECIDERCONFIG = DESCRIPTOR.message_types_by_name['OpenSpacePreStopDeciderConfig']
_OPENSPACEPRESTOPDECIDERCONFIG_STOPTYPE = _OPENSPACEPRESTOPDECIDERCONFIG.enum_types_by_name['StopType']
OpenSpacePreStopDeciderConfig = _reflection.GeneratedProtocolMessageType('OpenSpacePreStopDeciderConfig', (_message.Message,), {'DESCRIPTOR': _OPENSPACEPRESTOPDECIDERCONFIG, '__module__': 'modules.planning.tasks.open_space_pre_stop_decider.proto.open_space_pre_stop_decider_pb2'})
_sym_db.RegisterMessage(OpenSpacePreStopDeciderConfig)
if _descriptor._USE_C_DESCRIPTORS == False:
    DESCRIPTOR._options = None
    _OPENSPACEPRESTOPDECIDERCONFIG._serialized_start = 112
    _OPENSPACEPRESTOPDECIDERCONFIG._serialized_end = 382
    _OPENSPACEPRESTOPDECIDERCONFIG_STOPTYPE._serialized_start = 327
    _OPENSPACEPRESTOPDECIDERCONFIG_STOPTYPE._serialized_end = 382