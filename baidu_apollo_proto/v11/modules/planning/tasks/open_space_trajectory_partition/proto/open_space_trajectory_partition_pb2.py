"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
_sym_db = _symbol_database.Default()
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\nbmodules/planning/tasks/open_space_trajectory_partition/proto/open_space_trajectory_partition.proto\x12\x0fapollo.planning"\xce\x04\n"OpenSpaceTrajectoryPartitionConfig\x12\x18\n\x10gear_shift_max_t\x18\x01 \x01(\x01\x12\x19\n\x11gear_shift_unit_t\x18\x02 \x01(\x01\x12"\n\x1agear_shift_period_duration\x18\x03 \x01(\x01\x12\x1f\n\x17interpolated_pieces_num\x18\x04 \x01(\x04\x12"\n\x1ainitial_gear_check_horizon\x18\x05 \x01(\x04\x12\x1c\n\x14heading_search_range\x18\x06 \x01(\x01\x12\x1b\n\x13heading_track_range\x18\x07 \x01(\x01\x12$\n\x15distance_search_range\x18\x08 \x01(\x01:\x051e-06\x12"\n\x1aheading_offset_to_midpoint\x18\t \x01(\x01\x12\'\n\x1alateral_offset_to_midpoint\x18\n \x01(\x01:\x030.1\x12,\n\x1flongitudinal_offset_to_midpoint\x18\x0b \x01(\x01:\x030.1\x123\n%vehicle_box_iou_threshold_to_midpoint\x18\x0c \x01(\x01:\x040.95\x12-\n linear_velocity_threshold_on_ego\x18\r \x01(\x01:\x030.2\x12(\n\x19use_gear_shift_trajectory\x18\x0e \x01(\x08:\x05false\x12 \n\x15speed_replan_distance\x18\x0f \x01(\x01:\x012')
_OPENSPACETRAJECTORYPARTITIONCONFIG = DESCRIPTOR.message_types_by_name['OpenSpaceTrajectoryPartitionConfig']
OpenSpaceTrajectoryPartitionConfig = _reflection.GeneratedProtocolMessageType('OpenSpaceTrajectoryPartitionConfig', (_message.Message,), {'DESCRIPTOR': _OPENSPACETRAJECTORYPARTITIONCONFIG, '__module__': 'modules.planning.tasks.open_space_trajectory_partition.proto.open_space_trajectory_partition_pb2'})
_sym_db.RegisterMessage(OpenSpaceTrajectoryPartitionConfig)
if _descriptor._USE_C_DESCRIPTORS == False:
    DESCRIPTOR._options = None
    _OPENSPACETRAJECTORYPARTITIONCONFIG._serialized_start = 120
    _OPENSPACETRAJECTORYPARTITIONCONFIG._serialized_end = 710