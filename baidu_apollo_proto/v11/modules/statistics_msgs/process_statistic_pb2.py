"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
_sym_db = _symbol_database.Default()
from ...modules.common_msgs.basic_msgs import header_pb2 as modules_dot_common__msgs_dot_basic__msgs_dot_header__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n/modules/statistics_msgs/process_statistic.proto\x12\x18apollo.process_statistic\x1a+modules/common_msgs/basic_msgs/header.proto"\x8f\x01\n\x14ProcessStatisticConf\x12V\n\x0fgeneral_process\x18\x01 \x01(\x0b2=.apollo.process_statistic.ProcessStatisticConf.GeneralProcess\x1a\x1f\n\x0eGeneralProcess\x12\r\n\x05regex\x18\x01 \x03(\t"\x9d\x03\n\x0eProcessMetrics\x12%\n\x06header\x18\x01 \x01(\x0b2\x15.apollo.common.Header\x12L\n\rmainboard_dag\x18\x02 \x01(\x0b25.apollo.process_statistic.ProcessMetrics.MainboardDag\x12_\n\x17mainboard_process_group\x18\x03 \x01(\x0b2>.apollo.process_statistic.ProcessMetrics.MainboardProcessGroup\x12P\n\x0fgeneral_process\x18\x04 \x01(\x0b27.apollo.process_statistic.ProcessMetrics.GeneralProcess\x1a\x1c\n\x0cMainboardDag\x12\x0c\n\x04name\x18\x01 \x03(\t\x1a%\n\x15MainboardProcessGroup\x12\x0c\n\x04name\x18\x01 \x03(\t\x1a\x1e\n\x0eGeneralProcess\x12\x0c\n\x04name\x18\x01 \x03(\t')
_PROCESSSTATISTICCONF = DESCRIPTOR.message_types_by_name['ProcessStatisticConf']
_PROCESSSTATISTICCONF_GENERALPROCESS = _PROCESSSTATISTICCONF.nested_types_by_name['GeneralProcess']
_PROCESSMETRICS = DESCRIPTOR.message_types_by_name['ProcessMetrics']
_PROCESSMETRICS_MAINBOARDDAG = _PROCESSMETRICS.nested_types_by_name['MainboardDag']
_PROCESSMETRICS_MAINBOARDPROCESSGROUP = _PROCESSMETRICS.nested_types_by_name['MainboardProcessGroup']
_PROCESSMETRICS_GENERALPROCESS = _PROCESSMETRICS.nested_types_by_name['GeneralProcess']
ProcessStatisticConf = _reflection.GeneratedProtocolMessageType('ProcessStatisticConf', (_message.Message,), {'GeneralProcess': _reflection.GeneratedProtocolMessageType('GeneralProcess', (_message.Message,), {'DESCRIPTOR': _PROCESSSTATISTICCONF_GENERALPROCESS, '__module__': 'modules.statistics_msgs.process_statistic_pb2'}), 'DESCRIPTOR': _PROCESSSTATISTICCONF, '__module__': 'modules.statistics_msgs.process_statistic_pb2'})
_sym_db.RegisterMessage(ProcessStatisticConf)
_sym_db.RegisterMessage(ProcessStatisticConf.GeneralProcess)
ProcessMetrics = _reflection.GeneratedProtocolMessageType('ProcessMetrics', (_message.Message,), {'MainboardDag': _reflection.GeneratedProtocolMessageType('MainboardDag', (_message.Message,), {'DESCRIPTOR': _PROCESSMETRICS_MAINBOARDDAG, '__module__': 'modules.statistics_msgs.process_statistic_pb2'}), 'MainboardProcessGroup': _reflection.GeneratedProtocolMessageType('MainboardProcessGroup', (_message.Message,), {'DESCRIPTOR': _PROCESSMETRICS_MAINBOARDPROCESSGROUP, '__module__': 'modules.statistics_msgs.process_statistic_pb2'}), 'GeneralProcess': _reflection.GeneratedProtocolMessageType('GeneralProcess', (_message.Message,), {'DESCRIPTOR': _PROCESSMETRICS_GENERALPROCESS, '__module__': 'modules.statistics_msgs.process_statistic_pb2'}), 'DESCRIPTOR': _PROCESSMETRICS, '__module__': 'modules.statistics_msgs.process_statistic_pb2'})
_sym_db.RegisterMessage(ProcessMetrics)
_sym_db.RegisterMessage(ProcessMetrics.MainboardDag)
_sym_db.RegisterMessage(ProcessMetrics.MainboardProcessGroup)
_sym_db.RegisterMessage(ProcessMetrics.GeneralProcess)
if _descriptor._USE_C_DESCRIPTORS == False:
    DESCRIPTOR._options = None
    _PROCESSSTATISTICCONF._serialized_start = 123
    _PROCESSSTATISTICCONF._serialized_end = 266
    _PROCESSSTATISTICCONF_GENERALPROCESS._serialized_start = 235
    _PROCESSSTATISTICCONF_GENERALPROCESS._serialized_end = 266
    _PROCESSMETRICS._serialized_start = 269
    _PROCESSMETRICS._serialized_end = 682
    _PROCESSMETRICS_MAINBOARDDAG._serialized_start = 583
    _PROCESSMETRICS_MAINBOARDDAG._serialized_end = 611
    _PROCESSMETRICS_MAINBOARDPROCESSGROUP._serialized_start = 613
    _PROCESSMETRICS_MAINBOARDPROCESSGROUP._serialized_end = 650
    _PROCESSMETRICS_GENERALPROCESS._serialized_start = 652
    _PROCESSMETRICS_GENERALPROCESS._serialized_end = 682