"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
_sym_db = _symbol_database.Default()
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\nFmodules/planning/traffic_rules/traffic_light/proto/traffic_light.proto\x12\x0fapollo.planning"g\n\x12TrafficLightConfig\x12\x15\n\x07enabled\x18\x01 \x01(\x08:\x04true\x12\x18\n\rstop_distance\x18\x02 \x01(\x01:\x011\x12 \n\x15max_stop_deceleration\x18\x03 \x01(\x01:\x014')
_TRAFFICLIGHTCONFIG = DESCRIPTOR.message_types_by_name['TrafficLightConfig']
TrafficLightConfig = _reflection.GeneratedProtocolMessageType('TrafficLightConfig', (_message.Message,), {'DESCRIPTOR': _TRAFFICLIGHTCONFIG, '__module__': 'modules.planning.traffic_rules.traffic_light.proto.traffic_light_pb2'})
_sym_db.RegisterMessage(TrafficLightConfig)
if _descriptor._USE_C_DESCRIPTORS == False:
    DESCRIPTOR._options = None
    _TRAFFICLIGHTCONFIG._serialized_start = 91
    _TRAFFICLIGHTCONFIG._serialized_end = 194