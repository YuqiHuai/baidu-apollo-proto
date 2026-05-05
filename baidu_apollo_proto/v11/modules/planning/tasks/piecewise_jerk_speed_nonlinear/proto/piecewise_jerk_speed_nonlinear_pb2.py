"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
_sym_db = _symbol_database.Default()
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n`modules/planning/tasks/piecewise_jerk_speed_nonlinear/proto/piecewise_jerk_speed_nonlinear.proto\x12\x0fapollo.planning"\xbd\x03\n*PiecewiseJerkNonlinearSpeedOptimizerConfig\x12\x17\n\nacc_weight\x18\x01 \x01(\x01:\x03500\x12\x18\n\x0bjerk_weight\x18\x02 \x01(\x01:\x03100\x12\x1b\n\x0elat_acc_weight\x18\x03 \x01(\x01:\x03500\x12\x1e\n\x12s_potential_weight\x18\x04 \x01(\x01:\x0210\x12\x18\n\x0cref_v_weight\x18\x05 \x01(\x01:\x0210\x12\x18\n\x0cref_s_weight\x18\x06 \x01(\x01:\x0210\x12\x18\n\x0cend_s_weight\x18\x07 \x01(\x01:\x0210\x12\x18\n\x0cend_v_weight\x18\x08 \x01(\x01:\x0210\x12\x18\n\x0cend_a_weight\x18\t \x01(\x01:\x0210\x12\x1f\n\x13soft_s_bound_weight\x18\n \x01(\x01:\x0210\x12\x1c\n\x0euse_warm_start\x18d \x01(\x08:\x04true\x12)\n\x1ause_smoothed_dp_guide_line\x18e \x01(\x08:\x05false\x123\n%use_soft_bound_in_nonlinear_speed_opt\x18f \x01(\x08:\x04true')
_PIECEWISEJERKNONLINEARSPEEDOPTIMIZERCONFIG = DESCRIPTOR.message_types_by_name['PiecewiseJerkNonlinearSpeedOptimizerConfig']
PiecewiseJerkNonlinearSpeedOptimizerConfig = _reflection.GeneratedProtocolMessageType('PiecewiseJerkNonlinearSpeedOptimizerConfig', (_message.Message,), {'DESCRIPTOR': _PIECEWISEJERKNONLINEARSPEEDOPTIMIZERCONFIG, '__module__': 'modules.planning.tasks.piecewise_jerk_speed_nonlinear.proto.piecewise_jerk_speed_nonlinear_pb2'})
_sym_db.RegisterMessage(PiecewiseJerkNonlinearSpeedOptimizerConfig)
if _descriptor._USE_C_DESCRIPTORS == False:
    DESCRIPTOR._options = None
    _PIECEWISEJERKNONLINEARSPEEDOPTIMIZERCONFIG._serialized_start = 118
    _PIECEWISEJERKNONLINEARSPEEDOPTIMIZERCONFIG._serialized_end = 563