"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
_sym_db = _symbol_database.Default()
from ....modules.common_msgs.dreamview_msgs import simulation_world_pb2 as modules_dot_common__msgs_dot_dreamview__msgs_dot_simulation__world__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n+modules/dreamview_plus/proto/obstacle.proto\x12\x10apollo.dreamview\x1a9modules/common_msgs/dreamview_msgs/simulation_world.proto"\x9e\x02\n\tObstacles\x12*\n\x08obstacle\x18\x01 \x03(\x0b2\x18.apollo.dreamview.Object\x122\n\x10auto_driving_car\x18\x02 \x01(\x0b2\x18.apollo.dreamview.Object\x12P\n\x13sensor_measurements\x18\x03 \x03(\x0b23.apollo.dreamview.Obstacles.SensorMeasurementsEntry\x1a_\n\x17SensorMeasurementsEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x123\n\x05value\x18\x02 \x01(\x0b2$.apollo.dreamview.SensorMeasurements:\x028\x01')
_OBSTACLES = DESCRIPTOR.message_types_by_name['Obstacles']
_OBSTACLES_SENSORMEASUREMENTSENTRY = _OBSTACLES.nested_types_by_name['SensorMeasurementsEntry']
Obstacles = _reflection.GeneratedProtocolMessageType('Obstacles', (_message.Message,), {'SensorMeasurementsEntry': _reflection.GeneratedProtocolMessageType('SensorMeasurementsEntry', (_message.Message,), {'DESCRIPTOR': _OBSTACLES_SENSORMEASUREMENTSENTRY, '__module__': 'modules.dreamview_plus.proto.obstacle_pb2'}), 'DESCRIPTOR': _OBSTACLES, '__module__': 'modules.dreamview_plus.proto.obstacle_pb2'})
_sym_db.RegisterMessage(Obstacles)
_sym_db.RegisterMessage(Obstacles.SensorMeasurementsEntry)
if _descriptor._USE_C_DESCRIPTORS == False:
    DESCRIPTOR._options = None
    _OBSTACLES_SENSORMEASUREMENTSENTRY._options = None
    _OBSTACLES_SENSORMEASUREMENTSENTRY._serialized_options = b'8\x01'
    _OBSTACLES._serialized_start = 125
    _OBSTACLES._serialized_end = 411
    _OBSTACLES_SENSORMEASUREMENTSENTRY._serialized_start = 316
    _OBSTACLES_SENSORMEASUREMENTSENTRY._serialized_end = 411