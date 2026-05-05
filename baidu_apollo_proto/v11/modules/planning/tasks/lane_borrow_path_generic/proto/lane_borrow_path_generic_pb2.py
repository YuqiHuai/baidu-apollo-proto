"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
_sym_db = _symbol_database.Default()
from ......modules.planning.planning_base.proto import piecewise_jerk_path_config_pb2 as modules_dot_planning_dot_planning__base_dot_proto_dot_piecewise__jerk__path__config__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\nTmodules/planning/tasks/lane_borrow_path_generic/proto/lane_borrow_path_generic.proto\x12\x0fapollo.planning\x1aEmodules/planning/planning_base/proto/piecewise_jerk_path_config.proto"\x95\x03\n\x1bLaneBorrowPathGenericConfig\x12%\n\x17is_allow_lane_borrowing\x18\x01 \x01(\x08:\x04true\x12 \n\x15lane_borrow_max_speed\x18\x02 \x01(\x01:\x015\x126\n+long_term_blocking_obstacle_cycle_threshold\x18\x03 \x01(\x03:\x013\x12,\n\x1denable_extend_boundary_by_adc\x18\x04 \x01(\x08:\x05false\x12*\n\x1benable_ignore_boundary_type\x18\x05 \x01(\x08:\x05false\x12G\n\x15path_optimizer_config\x18\x06 \x01(\x0b2(.apollo.planning.PiecewiseJerkPathConfig\x12-\n"enable_nudge_destination_threshold\x18\x07 \x01(\x01:\x018\x12#\n\x15enable_active_trigger\x18\x08 \x01(\x08:\x04true')
_LANEBORROWPATHGENERICCONFIG = DESCRIPTOR.message_types_by_name['LaneBorrowPathGenericConfig']
LaneBorrowPathGenericConfig = _reflection.GeneratedProtocolMessageType('LaneBorrowPathGenericConfig', (_message.Message,), {'DESCRIPTOR': _LANEBORROWPATHGENERICCONFIG, '__module__': 'modules.planning.tasks.lane_borrow_path_generic.proto.lane_borrow_path_generic_pb2'})
_sym_db.RegisterMessage(LaneBorrowPathGenericConfig)
if _descriptor._USE_C_DESCRIPTORS == False:
    DESCRIPTOR._options = None
    _LANEBORROWPATHGENERICCONFIG._serialized_start = 177
    _LANEBORROWPATHGENERICCONFIG._serialized_end = 582