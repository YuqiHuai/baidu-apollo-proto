"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
_sym_db = _symbol_database.Default()
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\nNmodules/planning/planning_interface_base/scenario_base/proto/creep_stage.proto\x12\x0fapollo.planning"p\n\x10CreepStageConfig\x12\x19\n\x0emin_boundary_t\x18\x01 \x01(\x01:\x016\x12 \n\x13ignore_max_st_min_t\x18\x02 \x01(\x01:\x030.1\x12\x1f\n\x13ignore_min_st_min_s\x18\x03 \x01(\x01:\x0215')
_CREEPSTAGECONFIG = DESCRIPTOR.message_types_by_name['CreepStageConfig']
CreepStageConfig = _reflection.GeneratedProtocolMessageType('CreepStageConfig', (_message.Message,), {'DESCRIPTOR': _CREEPSTAGECONFIG, '__module__': 'modules.planning.planning_interface_base.scenario_base.proto.creep_stage_pb2'})
_sym_db.RegisterMessage(CreepStageConfig)
if _descriptor._USE_C_DESCRIPTORS == False:
    DESCRIPTOR._options = None
    _CREEPSTAGECONFIG._serialized_start = 99
    _CREEPSTAGECONFIG._serialized_end = 211