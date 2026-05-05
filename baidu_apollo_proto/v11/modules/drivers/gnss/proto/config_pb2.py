"""Generated protocol buffer code."""
from google.protobuf.internal import enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
_sym_db = _symbol_database.Default()
from .....modules.common_msgs.drivers_msgs import can_card_parameter_pb2 as modules_dot_common__msgs_dot_drivers__msgs_dot_can__card__parameter__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\'modules/drivers/gnss/proto/config.proto\x12\x1aapollo.drivers.gnss.config\x1a9modules/common_msgs/drivers_msgs/can_card_parameter.proto"\xba\x07\n\x06Stream\x129\n\x06format\x18\x01 \x01(\x0e2).apollo.drivers.gnss.config.Stream.Format\x12;\n\x06serial\x18\x02 \x01(\x0b2).apollo.drivers.gnss.config.Stream.SerialH\x00\x125\n\x03tcp\x18\x03 \x01(\x0b2&.apollo.drivers.gnss.config.Stream.TcpH\x00\x125\n\x03udp\x18\x04 \x01(\x0b2&.apollo.drivers.gnss.config.Stream.UdpH\x00\x129\n\x05ntrip\x18\x05 \x01(\x0b2(.apollo.drivers.gnss.config.Stream.NtripH\x00\x12E\n\x12can_card_parameter\x18\x06 \x01(\x0b2\'.apollo.drivers.canbus.CANCardParameterH\x00\x12\x15\n\rpush_location\x18\x07 \x01(\x08\x12\x1d\n\x0eis_data_stream\x18\x08 \x01(\x08:\x05false\x1a1\n\x06Serial\x12\x0e\n\x06device\x18\x01 \x01(\x0c\x12\x17\n\tbaud_rate\x18\x02 \x01(\x05:\x049600\x1a*\n\x03Tcp\x12\x0f\n\x07address\x18\x01 \x01(\x0c\x12\x12\n\x04port\x18\x02 \x01(\x05:\x043001\x1a*\n\x03Udp\x12\x0f\n\x07address\x18\x01 \x01(\x0c\x12\x12\n\x04port\x18\x02 \x01(\x05:\x043001\x1ax\n\x05Ntrip\x12\x0f\n\x07address\x18\x01 \x01(\x0c\x12\x12\n\x04port\x18\x02 \x01(\x05:\x042101\x12\x13\n\x0bmount_point\x18\x03 \x01(\x0c\x12\x0c\n\x04user\x18\x04 \x01(\x0c\x12\x10\n\x08password\x18\x05 \x01(\x0c\x12\x15\n\ttimeout_s\x18\x06 \x01(\r:\x0230"\x84\x02\n\x06Format\x12\x0b\n\x07UNKNOWN\x10\x00\x12\x08\n\x04NMEA\x10\x01\x12\x0b\n\x07RTCM_V2\x10\x02\x12\x0b\n\x07RTCM_V3\x10\x03\x12\x10\n\x0cNOVATEL_TEXT\x10\n\x12\x12\n\x0eNOVATEL_BINARY\x10\x0b\x12\x0e\n\nHUACE_TEXT\x10\x0c\x12\r\n\tHUACE_CAN\x10\r\x12\x11\n\rASENSING_TEXT\x10\x0e\x12\x13\n\x0fASENSING_BINARY\x10\x0f\x12\x10\n\x0cASENSING_CAN\x10\x10\x12\x0e\n\nUBLOX_TEXT\x10\x14\x12\x10\n\x0cUBLOX_BINARY\x10\x15\x12\x12\n\x0eBROADGNSS_TEXT\x10\x1e\x12\x14\n\x10BROADGNSS_BINARY\x10\x1fB\x06\n\x04type"+\n\rNovatelConfig\x12\x1a\n\x0fimu_orientation\x18\x01 \x01(\x05:\x015"\r\n\x0bUbloxConfig"U\n\x02TF\x12\x17\n\x08frame_id\x18\x01 \x01(\t:\x05world\x12\x1f\n\x0echild_frame_id\x18\x02 \x01(\t:\x07novatel\x12\x15\n\x06enable\x18\x03 \x01(\x08:\x05false"\xa0\x06\n\x06Config\x120\n\x04data\x18\x01 \x01(\x0b2".apollo.drivers.gnss.config.Stream\x123\n\x07command\x18\x02 \x01(\x0b2".apollo.drivers.gnss.config.Stream\x124\n\x08rtk_from\x18\x03 \x01(\x0b2".apollo.drivers.gnss.config.Stream\x122\n\x06rtk_to\x18\x04 \x01(\x0b2".apollo.drivers.gnss.config.Stream\x12\x16\n\x0elogin_commands\x18\x05 \x03(\x0c\x12\x17\n\x0flogout_commands\x18\x06 \x03(\x0c\x12C\n\x0enovatel_config\x18\x07 \x01(\x0b2).apollo.drivers.gnss.config.NovatelConfigH\x00\x12?\n\x0cublox_config\x18\x08 \x01(\x0b2\'.apollo.drivers.gnss.config.UbloxConfigH\x00\x12M\n\x11rtk_solution_type\x18\t \x01(\x0e22.apollo.drivers.gnss.config.Config.RtkSolutionType\x125\n\x08imu_type\x18\n \x01(\x0e2#.apollo.drivers.gnss.config.ImuType\x12\x12\n\nproj4_text\x18\x0b \x01(\t\x12*\n\x02tf\x18\x0c \x01(\x0b2\x1e.apollo.drivers.gnss.config.TF\x12\x18\n\x10wheel_parameters\x18\r \x01(\t\x12\x15\n\rgpsbin_folder\x18\x0e \x01(\t\x12\x1b\n\ruse_gnss_time\x18\x0f \x01(\x08:\x04true\x12 \n\x11auto_fill_gps_msg\x18\x10 \x01(\x08:\x05false"G\n\x0fRtkSolutionType\x12\x19\n\x15RTK_RECEIVER_SOLUTION\x10\x01\x12\x19\n\x15RTK_SOFTWARE_SOLUTION\x10\x02B\x0f\n\rdevice_config*\xa6\x01\n\x07ImuType\x12\r\n\tIMAR_FSAS\x10\r\x12\x0b\n\x07ISA100C\x10\x1a\x12\r\n\tADIS16488\x10\x1f\x12\x0b\n\x07STIM300\x10 \x12\n\n\x06ISA100\x10"\x12\x10\n\x0cISA100_400HZ\x10&\x12\x11\n\rISA100C_400HZ\x10\'\x12\x0e\n\nCPT_XW5651\x10(\x12\t\n\x05G320N\x10)\x12\t\n\x05UM442\x10*\x12\x0c\n\x08IAM20680\x109')
_IMUTYPE = DESCRIPTOR.enum_types_by_name['ImuType']
ImuType = enum_type_wrapper.EnumTypeWrapper(_IMUTYPE)
IMAR_FSAS = 13
ISA100C = 26
ADIS16488 = 31
STIM300 = 32
ISA100 = 34
ISA100_400HZ = 38
ISA100C_400HZ = 39
CPT_XW5651 = 40
G320N = 41
UM442 = 42
IAM20680 = 57
_STREAM = DESCRIPTOR.message_types_by_name['Stream']
_STREAM_SERIAL = _STREAM.nested_types_by_name['Serial']
_STREAM_TCP = _STREAM.nested_types_by_name['Tcp']
_STREAM_UDP = _STREAM.nested_types_by_name['Udp']
_STREAM_NTRIP = _STREAM.nested_types_by_name['Ntrip']
_NOVATELCONFIG = DESCRIPTOR.message_types_by_name['NovatelConfig']
_UBLOXCONFIG = DESCRIPTOR.message_types_by_name['UbloxConfig']
_TF = DESCRIPTOR.message_types_by_name['TF']
_CONFIG = DESCRIPTOR.message_types_by_name['Config']
_STREAM_FORMAT = _STREAM.enum_types_by_name['Format']
_CONFIG_RTKSOLUTIONTYPE = _CONFIG.enum_types_by_name['RtkSolutionType']
Stream = _reflection.GeneratedProtocolMessageType('Stream', (_message.Message,), {'Serial': _reflection.GeneratedProtocolMessageType('Serial', (_message.Message,), {'DESCRIPTOR': _STREAM_SERIAL, '__module__': 'modules.drivers.gnss.proto.config_pb2'}), 'Tcp': _reflection.GeneratedProtocolMessageType('Tcp', (_message.Message,), {'DESCRIPTOR': _STREAM_TCP, '__module__': 'modules.drivers.gnss.proto.config_pb2'}), 'Udp': _reflection.GeneratedProtocolMessageType('Udp', (_message.Message,), {'DESCRIPTOR': _STREAM_UDP, '__module__': 'modules.drivers.gnss.proto.config_pb2'}), 'Ntrip': _reflection.GeneratedProtocolMessageType('Ntrip', (_message.Message,), {'DESCRIPTOR': _STREAM_NTRIP, '__module__': 'modules.drivers.gnss.proto.config_pb2'}), 'DESCRIPTOR': _STREAM, '__module__': 'modules.drivers.gnss.proto.config_pb2'})
_sym_db.RegisterMessage(Stream)
_sym_db.RegisterMessage(Stream.Serial)
_sym_db.RegisterMessage(Stream.Tcp)
_sym_db.RegisterMessage(Stream.Udp)
_sym_db.RegisterMessage(Stream.Ntrip)
NovatelConfig = _reflection.GeneratedProtocolMessageType('NovatelConfig', (_message.Message,), {'DESCRIPTOR': _NOVATELCONFIG, '__module__': 'modules.drivers.gnss.proto.config_pb2'})
_sym_db.RegisterMessage(NovatelConfig)
UbloxConfig = _reflection.GeneratedProtocolMessageType('UbloxConfig', (_message.Message,), {'DESCRIPTOR': _UBLOXCONFIG, '__module__': 'modules.drivers.gnss.proto.config_pb2'})
_sym_db.RegisterMessage(UbloxConfig)
TF = _reflection.GeneratedProtocolMessageType('TF', (_message.Message,), {'DESCRIPTOR': _TF, '__module__': 'modules.drivers.gnss.proto.config_pb2'})
_sym_db.RegisterMessage(TF)
Config = _reflection.GeneratedProtocolMessageType('Config', (_message.Message,), {'DESCRIPTOR': _CONFIG, '__module__': 'modules.drivers.gnss.proto.config_pb2'})
_sym_db.RegisterMessage(Config)
if _descriptor._USE_C_DESCRIPTORS == False:
    DESCRIPTOR._options = None
    _IMUTYPE._serialized_start = 2038
    _IMUTYPE._serialized_end = 2204
    _STREAM._serialized_start = 131
    _STREAM._serialized_end = 1085
    _STREAM_SERIAL._serialized_start = 555
    _STREAM_SERIAL._serialized_end = 604
    _STREAM_TCP._serialized_start = 606
    _STREAM_TCP._serialized_end = 648
    _STREAM_UDP._serialized_start = 650
    _STREAM_UDP._serialized_end = 692
    _STREAM_NTRIP._serialized_start = 694
    _STREAM_NTRIP._serialized_end = 814
    _STREAM_FORMAT._serialized_start = 817
    _STREAM_FORMAT._serialized_end = 1077
    _NOVATELCONFIG._serialized_start = 1087
    _NOVATELCONFIG._serialized_end = 1130
    _UBLOXCONFIG._serialized_start = 1132
    _UBLOXCONFIG._serialized_end = 1145
    _TF._serialized_start = 1147
    _TF._serialized_end = 1232
    _CONFIG._serialized_start = 1235
    _CONFIG._serialized_end = 2035
    _CONFIG_RTKSOLUTIONTYPE._serialized_start = 1947
    _CONFIG_RTKSOLUTIONTYPE._serialized_end = 2018