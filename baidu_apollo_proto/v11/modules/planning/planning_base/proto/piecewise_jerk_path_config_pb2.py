"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
_sym_db = _symbol_database.Default()
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\nEmodules/planning/planning_base/proto/piecewise_jerk_path_config.proto\x12\x0fapollo.planning"\xcd\x02\n\x17PiecewiseJerkPathConfig\x12\x13\n\x08l_weight\x18\x01 \x01(\x01:\x011\x12\x16\n\tdl_weight\x18\x02 \x01(\x01:\x03100\x12\x18\n\nddl_weight\x18\x03 \x01(\x01:\x041000\x12\x1a\n\x0bdddl_weight\x18\x04 \x01(\x01:\x0510000\x12"\n\x17path_reference_l_weight\x18\x05 \x01(\x01:\x010\x12 \n\x12weight_end_state_l\x18\x06 \x01(\x01:\x041000\x12\x1e\n\x13weight_end_state_dl\x18\x07 \x01(\x01:\x010\x12\x1f\n\x14weight_end_state_ddl\x18\x08 \x01(\x01:\x010\x12+\n lateral_derivative_bound_default\x18\t \x01(\x01:\x012\x12\x1b\n\rmax_iteration\x18\n \x01(\x03:\x044000')
_PIECEWISEJERKPATHCONFIG = DESCRIPTOR.message_types_by_name['PiecewiseJerkPathConfig']
PiecewiseJerkPathConfig = _reflection.GeneratedProtocolMessageType('PiecewiseJerkPathConfig', (_message.Message,), {'DESCRIPTOR': _PIECEWISEJERKPATHCONFIG, '__module__': 'modules.planning.planning_base.proto.piecewise_jerk_path_config_pb2'})
_sym_db.RegisterMessage(PiecewiseJerkPathConfig)
if _descriptor._USE_C_DESCRIPTORS == False:
    DESCRIPTOR._options = None
    _PIECEWISEJERKPATHCONFIG._serialized_start = 91
    _PIECEWISEJERKPATHCONFIG._serialized_end = 424