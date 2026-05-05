"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
_sym_db = _symbol_database.Default()
from ...modules.common_msgs.basic_msgs import header_pb2 as modules_dot_common__msgs_dot_basic__msgs_dot_header__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n/modules/statistics_msgs/latency_statistic.proto\x12\x18apollo.latency_statistic\x1a+modules/common_msgs/basic_msgs/header.proto"\xdc\x04\n\x0eLatencyMetrics\x12%\n\x06header\x18\x01 \x01(\x0b2\x15.apollo.common.Header\x12H\n\x11lidar_compensator\x18\x02 \x01(\x0b2-.apollo.latency_statistic.LatencyMetrics.Item\x12A\n\nperception\x18\x03 \x01(\x0b2-.apollo.latency_statistic.LatencyMetrics.Item\x12A\n\nprediction\x18\x04 \x01(\x0b2-.apollo.latency_statistic.LatencyMetrics.Item\x12?\n\x08planning\x18\x05 \x01(\x0b2-.apollo.latency_statistic.LatencyMetrics.Item\x12>\n\x07control\x18\x06 \x01(\x0b2-.apollo.latency_statistic.LatencyMetrics.Item\x1aD\n\x06Metric\x12\x0b\n\x03min\x18\x01 \x01(\r\x12\x0b\n\x03max\x18\x02 \x01(\r\x12\x0b\n\x03avg\x18\x03 \x01(\r\x12\x13\n\x0bsample_size\x18\x04 \x01(\r\x1a\x8b\x01\n\x04Item\x12@\n\x07proc_ms\x18\x01 \x01(\x0b2/.apollo.latency_statistic.LatencyMetrics.Metric\x12A\n\x08chain_ms\x18\x02 \x01(\x0b2/.apollo.latency_statistic.LatencyMetrics.Metric')
_LATENCYMETRICS = DESCRIPTOR.message_types_by_name['LatencyMetrics']
_LATENCYMETRICS_METRIC = _LATENCYMETRICS.nested_types_by_name['Metric']
_LATENCYMETRICS_ITEM = _LATENCYMETRICS.nested_types_by_name['Item']
LatencyMetrics = _reflection.GeneratedProtocolMessageType('LatencyMetrics', (_message.Message,), {'Metric': _reflection.GeneratedProtocolMessageType('Metric', (_message.Message,), {'DESCRIPTOR': _LATENCYMETRICS_METRIC, '__module__': 'modules.statistics_msgs.latency_statistic_pb2'}), 'Item': _reflection.GeneratedProtocolMessageType('Item', (_message.Message,), {'DESCRIPTOR': _LATENCYMETRICS_ITEM, '__module__': 'modules.statistics_msgs.latency_statistic_pb2'}), 'DESCRIPTOR': _LATENCYMETRICS, '__module__': 'modules.statistics_msgs.latency_statistic_pb2'})
_sym_db.RegisterMessage(LatencyMetrics)
_sym_db.RegisterMessage(LatencyMetrics.Metric)
_sym_db.RegisterMessage(LatencyMetrics.Item)
if _descriptor._USE_C_DESCRIPTORS == False:
    DESCRIPTOR._options = None
    _LATENCYMETRICS._serialized_start = 123
    _LATENCYMETRICS._serialized_end = 727
    _LATENCYMETRICS_METRIC._serialized_start = 517
    _LATENCYMETRICS_METRIC._serialized_end = 585
    _LATENCYMETRICS_ITEM._serialized_start = 588
    _LATENCYMETRICS_ITEM._serialized_end = 727