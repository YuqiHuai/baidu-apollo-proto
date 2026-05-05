"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
_sym_db = _symbol_database.Default()
from ......modules.planning.planning_base.proto import piecewise_jerk_path_config_pb2 as modules_dot_planning_dot_planning__base_dot_proto_dot_piecewise__jerk__path__config__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n@modules/planning/tasks/pull_over_path/proto/pull_over_path.proto\x12\x0fapollo.planning\x1aEmodules/planning/planning_base/proto/piecewise_jerk_path_config.proto"\x84\x05\n\x12PullOverPathConfig\x12G\n\x15path_optimizer_config\x18\x01 \x01(\x0b2(.apollo.planning.PiecewiseJerkPathConfig\x12(\n\x1apull_over_road_edge_buffer\x18\x02 \x01(\x01:\x040.15\x12\x1c\n\x10pull_over_weight\x18\x03 \x01(\x01:\x0210\x12:\n-pull_over_approach_lon_distance_adjust_factor\x18\x05 \x01(\x01:\x031.5\x12/\n#pull_over_destination_to_adc_buffer\x18\x06 \x01(\x01:\x0225\x123\n\'pull_over_destination_to_pathend_buffer\x18\x07 \x01(\x01:\x0210\x12^\n\x13pull_over_direction\x18\x08 \x01(\x0e25.apollo.planning.PullOverPathConfig.PullOverDirection:\nRIGHT_SIDE\x12]\n\x12pull_over_position\x18\t \x01(\x0e24.apollo.planning.PullOverPathConfig.PullOverPosition:\x0bDESTINATION"A\n\x11PullOverDirection\x12\r\n\tLEFT_SIDE\x10\x00\x12\x0e\n\nRIGHT_SIDE\x10\x01\x12\r\n\tBOTH_SIDE\x10\x02"9\n\x10PullOverPosition\x12\x14\n\x10NEAREST_POSITION\x10\x00\x12\x0f\n\x0bDESTINATION\x10\x01')
_PULLOVERPATHCONFIG = DESCRIPTOR.message_types_by_name['PullOverPathConfig']
_PULLOVERPATHCONFIG_PULLOVERDIRECTION = _PULLOVERPATHCONFIG.enum_types_by_name['PullOverDirection']
_PULLOVERPATHCONFIG_PULLOVERPOSITION = _PULLOVERPATHCONFIG.enum_types_by_name['PullOverPosition']
PullOverPathConfig = _reflection.GeneratedProtocolMessageType('PullOverPathConfig', (_message.Message,), {'DESCRIPTOR': _PULLOVERPATHCONFIG, '__module__': 'modules.planning.tasks.pull_over_path.proto.pull_over_path_pb2'})
_sym_db.RegisterMessage(PullOverPathConfig)
if _descriptor._USE_C_DESCRIPTORS == False:
    DESCRIPTOR._options = None
    _PULLOVERPATHCONFIG._serialized_start = 157
    _PULLOVERPATHCONFIG._serialized_end = 801
    _PULLOVERPATHCONFIG_PULLOVERDIRECTION._serialized_start = 677
    _PULLOVERPATHCONFIG_PULLOVERDIRECTION._serialized_end = 742
    _PULLOVERPATHCONFIG_PULLOVERPOSITION._serialized_start = 744
    _PULLOVERPATHCONFIG_PULLOVERPOSITION._serialized_end = 801