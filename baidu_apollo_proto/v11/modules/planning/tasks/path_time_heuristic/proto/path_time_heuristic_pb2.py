"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
_sym_db = _symbol_database.Default()
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\nJmodules/planning/tasks/path_time_heuristic/proto/path_time_heuristic.proto\x12\x0fapollo.planning"\xb5\x01\n\x1dSpeedHeuristicOptimizerConfig\x12G\n\x14default_speed_config\x18\x01 \x01(\x0b2).apollo.planning.DpStSpeedOptimizerConfig\x12K\n\x18lane_change_speed_config\x18\x02 \x01(\x0b2).apollo.planning.DpStSpeedOptimizerConfig"\xa5\x07\n\x18DpStSpeedOptimizerConfig\x12\x11\n\x06unit_t\x18\x01 \x01(\x01:\x011\x12\x1d\n\x11dense_dimension_s\x18\x02 \x01(\x05:\x0241\x12\x19\n\x0cdense_unit_s\x18\x03 \x01(\x01:\x030.5\x12\x18\n\rsparse_unit_s\x18\x04 \x01(\x01:\x011\x12\x17\n\x0cspeed_weight\x18\n \x01(\x01:\x010\x12\x18\n\x0caccel_weight\x18\x0b \x01(\x01:\x0210\x12\x17\n\x0bjerk_weight\x18\x0c \x01(\x01:\x0210\x12\x1a\n\x0fobstacle_weight\x18\r \x01(\x01:\x011\x12\x1b\n\x10reference_weight\x18\x0e \x01(\x01:\x010\x12\x19\n\x0ego_down_buffer\x18\x0f \x01(\x01:\x015\x12\x17\n\x0cgo_up_buffer\x18\x10 \x01(\x01:\x015\x12*\n\x15default_obstacle_cost\x18\x14 \x01(\x01:\x0b10000000000\x12\x1d\n\x12default_speed_cost\x18\x1f \x01(\x01:\x011\x12 \n\x14exceed_speed_penalty\x18  \x01(\x01:\x0210\x12\x1e\n\x11low_speed_penalty\x18! \x01(\x01:\x032.5\x12"\n\x17reference_speed_penalty\x18" \x01(\x01:\x011\x12(\n\x1ckeep_clear_low_speed_penalty\x18# \x01(\x01:\x0210\x12\x18\n\raccel_penalty\x18( \x01(\x01:\x012\x12\x18\n\rdecel_penalty\x18) \x01(\x01:\x012\x12\x1e\n\x13positive_jerk_coeff\x182 \x01(\x01:\x011\x12 \n\x13negative_jerk_coeff\x183 \x01(\x01:\x03300\x12\x1d\n\x10max_acceleration\x18< \x01(\x01:\x034.5\x12\x1e\n\x10max_deceleration\x18= \x01(\x01:\x04-4.5\x12\x1b\n\x10safe_time_buffer\x18F \x01(\x01:\x013\x12\x19\n\rsafe_distance\x18G \x01(\x01:\x0220\x12$\n\x19spatial_potential_penalty\x18P \x01(\x01:\x011\x12\x1f\n\x10is_lane_changing\x18Q \x01(\x08:\x05false\x121\n"enable_multi_thread_in_dp_st_graph\x18R \x01(\x08:\x05false\x12\'\n\x19enable_dp_reference_speed\x18S \x01(\x08:\x04true')
_SPEEDHEURISTICOPTIMIZERCONFIG = DESCRIPTOR.message_types_by_name['SpeedHeuristicOptimizerConfig']
_DPSTSPEEDOPTIMIZERCONFIG = DESCRIPTOR.message_types_by_name['DpStSpeedOptimizerConfig']
SpeedHeuristicOptimizerConfig = _reflection.GeneratedProtocolMessageType('SpeedHeuristicOptimizerConfig', (_message.Message,), {'DESCRIPTOR': _SPEEDHEURISTICOPTIMIZERCONFIG, '__module__': 'modules.planning.tasks.path_time_heuristic.proto.path_time_heuristic_pb2'})
_sym_db.RegisterMessage(SpeedHeuristicOptimizerConfig)
DpStSpeedOptimizerConfig = _reflection.GeneratedProtocolMessageType('DpStSpeedOptimizerConfig', (_message.Message,), {'DESCRIPTOR': _DPSTSPEEDOPTIMIZERCONFIG, '__module__': 'modules.planning.tasks.path_time_heuristic.proto.path_time_heuristic_pb2'})
_sym_db.RegisterMessage(DpStSpeedOptimizerConfig)
if _descriptor._USE_C_DESCRIPTORS == False:
    DESCRIPTOR._options = None
    _SPEEDHEURISTICOPTIMIZERCONFIG._serialized_start = 96
    _SPEEDHEURISTICOPTIMIZERCONFIG._serialized_end = 277
    _DPSTSPEEDOPTIMIZERCONFIG._serialized_start = 280
    _DPSTSPEEDOPTIMIZERCONFIG._serialized_end = 1213