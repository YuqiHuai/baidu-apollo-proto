"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
_sym_db = _symbol_database.Default()
from ......modules.planning.planning_base.proto import piecewise_jerk_path_config_pb2 as modules_dot_planning_dot_planning__base_dot_proto_dot_piecewise__jerk__path__config__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\nDmodules/planning/tasks/lane_change_path/proto/lane_change_path.proto\x12\x0fapollo.planning\x1aEmodules/planning/planning_base/proto/piecewise_jerk_path_config.proto"\xed\x01\n\x14LaneChangePathConfig\x12G\n\x15path_optimizer_config\x18\x01 \x01(\x0b2(.apollo.planning.PiecewiseJerkPathConfig\x12\x19\n\x11extend_adc_buffer\x18\x02 \x01(\x01\x12$\n\x1cchange_lane_fail_freeze_time\x18\x03 \x01(\x01\x12\'\n\x1fchange_lane_success_freeze_time\x18\x04 \x01(\x01\x12"\n\x1alane_change_prepare_length\x18\x05 \x01(\x01')
_LANECHANGEPATHCONFIG = DESCRIPTOR.message_types_by_name['LaneChangePathConfig']
LaneChangePathConfig = _reflection.GeneratedProtocolMessageType('LaneChangePathConfig', (_message.Message,), {'DESCRIPTOR': _LANECHANGEPATHCONFIG, '__module__': 'modules.planning.tasks.lane_change_path.proto.lane_change_path_pb2'})
_sym_db.RegisterMessage(LaneChangePathConfig)
if _descriptor._USE_C_DESCRIPTORS == False:
    DESCRIPTOR._options = None
    _LANECHANGEPATHCONFIG._serialized_start = 161
    _LANECHANGEPATHCONFIG._serialized_end = 398