"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
_sym_db = _symbol_database.Default()
from ......modules.common_msgs.sensor_msgs import conti_radar_pb2 as modules_dot_common__msgs_dot_sensor__msgs_dot_conti__radar__pb2
from ......modules.common_msgs.drivers_msgs import can_card_parameter_pb2 as modules_dot_common__msgs_dot_drivers__msgs_dot_can__card__parameter__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n>modules/drivers/radar/conti_radar/proto/conti_radar_conf.proto\x12\x1aapollo.drivers.conti_radar\x1a1modules/common_msgs/sensor_msgs/conti_radar.proto\x1a9modules/common_msgs/drivers_msgs/can_card_parameter.proto"\xb6\x01\n\x07CanConf\x12C\n\x12can_card_parameter\x18\x01 \x01(\x0b2\'.apollo.drivers.canbus.CANCardParameter\x12 \n\x11enable_debug_mode\x18\x02 \x01(\x08:\x05false\x12"\n\x13enable_receiver_log\x18\x03 \x01(\x08:\x05false\x12 \n\x11enable_sender_log\x18\x04 \x01(\x08:\x05false"\xf4\x05\n\tRadarConf\x12!\n\x12max_distance_valid\x18\x01 \x01(\x08:\x05false\x12\x1e\n\x0fsensor_id_valid\x18\x02 \x01(\x08:\x05false\x12 \n\x11radar_power_valid\x18\x03 \x01(\x08:\x05false\x12\x1f\n\x11output_type_valid\x18\x04 \x01(\x08:\x04true\x12 \n\x12send_quality_valid\x18\x05 \x01(\x08:\x04true\x12!\n\x13send_ext_info_valid\x18\x06 \x01(\x08:\x04true\x12\x1f\n\x10sort_index_valid\x18\x07 \x01(\x08:\x05false\x12 \n\x12store_in_nvm_valid\x18\x08 \x01(\x08:\x04true\x12\x1f\n\x10ctrl_relay_valid\x18\t \x01(\x08:\x05false\x12!\n\x13rcs_threshold_valid\x18\n \x01(\x08:\x04true\x12\x19\n\x0cmax_distance\x18\x0b \x01(\r:\x03248\x12\x14\n\tsensor_id\x18\x0c \x01(\r:\x010\x12S\n\x0boutput_type\x18\r \x01(\x0e2).apollo.drivers.RadarState_201.OutputType:\x13OUTPUT_TYPE_OBJECTS\x12\x16\n\x0bradar_power\x18\x0e \x01(\r:\x010\x12\x15\n\nctrl_relay\x18\x0f \x01(\r:\x010\x12\x1b\n\rsend_ext_info\x18\x10 \x01(\x08:\x04true\x12\x1a\n\x0csend_quality\x18\x11 \x01(\x08:\x04true\x12\x15\n\nsort_index\x18\x12 \x01(\r:\x010\x12\x17\n\x0cstore_in_nvm\x18\x13 \x01(\r:\x011\x12Z\n\rrcs_threshold\x18\x14 \x01(\x0e2+.apollo.drivers.RadarState_201.RcsThreshold:\x16RCS_THRESHOLD_STANDARD\x12\x1b\n\x13input_send_interval\x18\x15 \x01(\x04"\x99\x01\n\x0eContiRadarConf\x125\n\x08can_conf\x18\x01 \x01(\x0b2#.apollo.drivers.conti_radar.CanConf\x129\n\nradar_conf\x18\x02 \x01(\x0b2%.apollo.drivers.conti_radar.RadarConf\x12\x15\n\rradar_channel\x18\x03 \x01(\t')
_CANCONF = DESCRIPTOR.message_types_by_name['CanConf']
_RADARCONF = DESCRIPTOR.message_types_by_name['RadarConf']
_CONTIRADARCONF = DESCRIPTOR.message_types_by_name['ContiRadarConf']
CanConf = _reflection.GeneratedProtocolMessageType('CanConf', (_message.Message,), {'DESCRIPTOR': _CANCONF, '__module__': 'modules.drivers.radar.conti_radar.proto.conti_radar_conf_pb2'})
_sym_db.RegisterMessage(CanConf)
RadarConf = _reflection.GeneratedProtocolMessageType('RadarConf', (_message.Message,), {'DESCRIPTOR': _RADARCONF, '__module__': 'modules.drivers.radar.conti_radar.proto.conti_radar_conf_pb2'})
_sym_db.RegisterMessage(RadarConf)
ContiRadarConf = _reflection.GeneratedProtocolMessageType('ContiRadarConf', (_message.Message,), {'DESCRIPTOR': _CONTIRADARCONF, '__module__': 'modules.drivers.radar.conti_radar.proto.conti_radar_conf_pb2'})
_sym_db.RegisterMessage(ContiRadarConf)
if _descriptor._USE_C_DESCRIPTORS == False:
    DESCRIPTOR._options = None
    _CANCONF._serialized_start = 205
    _CANCONF._serialized_end = 387
    _RADARCONF._serialized_start = 390
    _RADARCONF._serialized_end = 1146
    _CONTIRADARCONF._serialized_start = 1149
    _CONTIRADARCONF._serialized_end = 1302