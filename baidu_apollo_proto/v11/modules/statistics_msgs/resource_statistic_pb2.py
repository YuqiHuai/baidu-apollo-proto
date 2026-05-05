"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
_sym_db = _symbol_database.Default()
from ...modules.common_msgs.basic_msgs import header_pb2 as modules_dot_common__msgs_dot_basic__msgs_dot_header__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n0modules/statistics_msgs/resource_statistic.proto\x12\x19apollo.resource_statistic\x1a+modules/common_msgs/basic_msgs/header.proto"\x81\x01\n\x15ResourceStatisticConf\x12L\n\tdisk_conf\x18\x01 \x01(\x0b29.apollo.resource_statistic.ResourceStatisticConf.DiskConf\x1a\x1a\n\x08DiskConf\x12\x0e\n\x06device\x18\x01 \x03(\t"/\n\tCpuMetric\x12\r\n\x05usage\x18\x01 \x01(\x02\x12\x13\n\x0btemperature\x18\x02 \x01(\x02"V\n\x0cMemoryMetric\x12\x0f\n\x07used_mb\x18\x01 \x01(\x04\x12\x14\n\x0cavailable_mb\x18\x02 \x01(\x04\x12\x10\n\x08total_mb\x18\x03 \x01(\x04\x12\r\n\x05usage\x18\x04 \x01(\x02"\xb9\x01\n\nDiskMetric\x12=\n\x07devices\x18\x01 \x03(\x0b2,.apollo.resource_statistic.DiskMetric.Metric\x1al\n\x06Metric\x12\x0c\n\x04name\x18\x01 \x02(\t\x12\x0f\n\x07used_gb\x18\x02 \x01(\r\x12\x14\n\x0cavailable_gb\x18\x03 \x01(\r\x12\x10\n\x08total_gb\x18\x04 \x01(\r\x12\r\n\x05usage\x18\x05 \x01(\x02\x12\x0c\n\x04load\x18\x06 \x01(\x02"/\n\tGpuMetric\x12\r\n\x05usage\x18\x02 \x01(\x02\x12\x13\n\x0btemperature\x18\x03 \x01(\x02"\x8c\x02\n\x0fResourceMetrics\x12%\n\x06header\x18\x01 \x01(\x0b2\x15.apollo.common.Header\x121\n\x03cpu\x18\x02 \x01(\x0b2$.apollo.resource_statistic.CpuMetric\x127\n\x06memory\x18\x03 \x01(\x0b2\'.apollo.resource_statistic.MemoryMetric\x123\n\x04disk\x18\x04 \x01(\x0b2%.apollo.resource_statistic.DiskMetric\x121\n\x03gpu\x18\x05 \x01(\x0b2$.apollo.resource_statistic.GpuMetric')
_RESOURCESTATISTICCONF = DESCRIPTOR.message_types_by_name['ResourceStatisticConf']
_RESOURCESTATISTICCONF_DISKCONF = _RESOURCESTATISTICCONF.nested_types_by_name['DiskConf']
_CPUMETRIC = DESCRIPTOR.message_types_by_name['CpuMetric']
_MEMORYMETRIC = DESCRIPTOR.message_types_by_name['MemoryMetric']
_DISKMETRIC = DESCRIPTOR.message_types_by_name['DiskMetric']
_DISKMETRIC_METRIC = _DISKMETRIC.nested_types_by_name['Metric']
_GPUMETRIC = DESCRIPTOR.message_types_by_name['GpuMetric']
_RESOURCEMETRICS = DESCRIPTOR.message_types_by_name['ResourceMetrics']
ResourceStatisticConf = _reflection.GeneratedProtocolMessageType('ResourceStatisticConf', (_message.Message,), {'DiskConf': _reflection.GeneratedProtocolMessageType('DiskConf', (_message.Message,), {'DESCRIPTOR': _RESOURCESTATISTICCONF_DISKCONF, '__module__': 'modules.statistics_msgs.resource_statistic_pb2'}), 'DESCRIPTOR': _RESOURCESTATISTICCONF, '__module__': 'modules.statistics_msgs.resource_statistic_pb2'})
_sym_db.RegisterMessage(ResourceStatisticConf)
_sym_db.RegisterMessage(ResourceStatisticConf.DiskConf)
CpuMetric = _reflection.GeneratedProtocolMessageType('CpuMetric', (_message.Message,), {'DESCRIPTOR': _CPUMETRIC, '__module__': 'modules.statistics_msgs.resource_statistic_pb2'})
_sym_db.RegisterMessage(CpuMetric)
MemoryMetric = _reflection.GeneratedProtocolMessageType('MemoryMetric', (_message.Message,), {'DESCRIPTOR': _MEMORYMETRIC, '__module__': 'modules.statistics_msgs.resource_statistic_pb2'})
_sym_db.RegisterMessage(MemoryMetric)
DiskMetric = _reflection.GeneratedProtocolMessageType('DiskMetric', (_message.Message,), {'Metric': _reflection.GeneratedProtocolMessageType('Metric', (_message.Message,), {'DESCRIPTOR': _DISKMETRIC_METRIC, '__module__': 'modules.statistics_msgs.resource_statistic_pb2'}), 'DESCRIPTOR': _DISKMETRIC, '__module__': 'modules.statistics_msgs.resource_statistic_pb2'})
_sym_db.RegisterMessage(DiskMetric)
_sym_db.RegisterMessage(DiskMetric.Metric)
GpuMetric = _reflection.GeneratedProtocolMessageType('GpuMetric', (_message.Message,), {'DESCRIPTOR': _GPUMETRIC, '__module__': 'modules.statistics_msgs.resource_statistic_pb2'})
_sym_db.RegisterMessage(GpuMetric)
ResourceMetrics = _reflection.GeneratedProtocolMessageType('ResourceMetrics', (_message.Message,), {'DESCRIPTOR': _RESOURCEMETRICS, '__module__': 'modules.statistics_msgs.resource_statistic_pb2'})
_sym_db.RegisterMessage(ResourceMetrics)
if _descriptor._USE_C_DESCRIPTORS == False:
    DESCRIPTOR._options = None
    _RESOURCESTATISTICCONF._serialized_start = 125
    _RESOURCESTATISTICCONF._serialized_end = 254
    _RESOURCESTATISTICCONF_DISKCONF._serialized_start = 228
    _RESOURCESTATISTICCONF_DISKCONF._serialized_end = 254
    _CPUMETRIC._serialized_start = 256
    _CPUMETRIC._serialized_end = 303
    _MEMORYMETRIC._serialized_start = 305
    _MEMORYMETRIC._serialized_end = 391
    _DISKMETRIC._serialized_start = 394
    _DISKMETRIC._serialized_end = 579
    _DISKMETRIC_METRIC._serialized_start = 471
    _DISKMETRIC_METRIC._serialized_end = 579
    _GPUMETRIC._serialized_start = 581
    _GPUMETRIC._serialized_end = 628
    _RESOURCEMETRICS._serialized_start = 631
    _RESOURCEMETRICS._serialized_end = 899