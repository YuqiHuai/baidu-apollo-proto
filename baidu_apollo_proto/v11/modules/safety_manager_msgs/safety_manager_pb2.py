"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
_sym_db = _symbol_database.Default()
from ...modules.common_msgs.basic_msgs import header_pb2 as modules_dot_common__msgs_dot_basic__msgs_dot_header__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n0modules/safety_manager_msgs/safety_manager.proto\x12\x15apollo.safety_manager\x1a+modules/common_msgs/basic_msgs/header.proto"7\n\x06Filter\x12\x17\n\x0frequired_cycles\x18\x01 \x02(\r\x12\x14\n\x0ctotal_cycles\x18\x02 \x02(\r"}\n\nSafetyRule\x12\x0f\n\x07timeout\x18\x01 \x01(\x01\x12\x10\n\x08duration\x18\x02 \x01(\x01\x12-\n\x06filter\x18\x03 \x01(\x0b2\x1d.apollo.safety_manager.Filter\x12\x1d\n\x12fault_removed_secs\x18\x04 \x01(\x05:\x015"\x7f\n\x07Matcher\x12\x0c\n\x04name\x18\x01 \x03(\t\x12\x10\n\x08contains\x18\x02 \x03(\t\x12\x0e\n\x06prefix\x18\x03 \x03(\t\x12\r\n\x05regex\x18\x04 \x03(\t\x12\x19\n\x11tags_contains_one\x18\x05 \x03(\t\x12\x1a\n\x12tags_contains_many\x18\x06 \x03(\t"o\n\x0bRuleMatcher\x12/\n\x07matcher\x18\x01 \x02(\x0b2\x1e.apollo.safety_manager.Matcher\x12/\n\x04rule\x18\x02 \x02(\x0b2!.apollo.safety_manager.SafetyRule"K\n\x0fRuleMatcherList\x128\n\x0crule_matcher\x18\x01 \x03(\x0b2".apollo.safety_manager.RuleMatcher"\xbb\x05\n\x0cSafetyStatus\x12%\n\x06header\x18\x01 \x01(\x0b2\x15.apollo.common.Header\x12\x0c\n\x04name\x18\x02 \x02(\t\x12:\n\x06status\x18\x03 \x02(\x0e2*.apollo.safety_manager.SafetyStatus.Status\x12\x0f\n\x07message\x18\x04 \x01(\t\x12?\n\x06values\x18\x05 \x03(\x0b2/.apollo.safety_manager.SafetyStatus.ValuesEntry\x12\x0c\n\x04tags\x18\x06 \x03(\t\x12/\n\x04rule\x18\x07 \x01(\x0b2!.apollo.safety_manager.SafetyRule\x127\n\x05items\x18\x08 \x03(\x0b2(.apollo.safety_manager.SafetyStatus.Item\x1a\xc4\x01\n\x04Item\x12\x0c\n\x04name\x18\x01 \x02(\t\x12\x0c\n\x04code\x18\x02 \x01(\x04\x12\x0c\n\x04type\x18\x03 \x01(\t\x12\r\n\x05level\x18\x04 \x01(\t\x12\x12\n\nconditions\x18\x05 \x01(\t\x12\x13\n\x0bdescription\x18\x06 \x01(\t\x12:\n\x06status\x18\x07 \x01(\x0e2*.apollo.safety_manager.SafetyStatus.Status\x12\r\n\x05value\x18\x08 \x01(\t\x12\x0f\n\x07message\x18\t \x01(\t\x1a-\n\x0bValuesEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\t:\x028\x01"z\n\x06Status\x12\x06\n\x02OK\x10\x01\x12\x10\n\x0cWARN_PENDING\x10\x02\x12\x11\n\rERROR_PENDING\x10\x03\x12\x11\n\rFATAL_PENDING\x10\x04\x12\x08\n\x04WARN\x10\x05\x12\t\n\x05ERROR\x10\x06\x12\t\n\x05FATAL\x10\x07\x12\x10\n\x0cWAIT_REMOVED\x10\x08"t\n\x10SafetyStatusAggr\x12%\n\x06header\x18\x01 \x01(\x0b2\x15.apollo.common.Header\x129\n\x0cstatus_array\x18\x02 \x03(\x0b2#.apollo.safety_manager.SafetyStatus"y\n\x0eSafetyDecision\x12%\n\x06header\x18\x01 \x01(\x0b2\x15.apollo.common.Header\x12 \n\x18safety_mode_trigger_time\x18\x02 \x01(\x01\x12\x1e\n\x16require_emergency_stop\x18\x03 \x01(\x08"<\n\x18SafetyFaultRemoveRequest\x12\x11\n\ttimestamp\x18\x01 \x02(\x01\x12\r\n\x05names\x18\x02 \x03(\t"=\n\x19SafetyFaultRemoveResponse\x12\x0f\n\x07success\x18\x01 \x02(\x08\x12\x0f\n\x07message\x18\x02 \x01(\t')
_FILTER = DESCRIPTOR.message_types_by_name['Filter']
_SAFETYRULE = DESCRIPTOR.message_types_by_name['SafetyRule']
_MATCHER = DESCRIPTOR.message_types_by_name['Matcher']
_RULEMATCHER = DESCRIPTOR.message_types_by_name['RuleMatcher']
_RULEMATCHERLIST = DESCRIPTOR.message_types_by_name['RuleMatcherList']
_SAFETYSTATUS = DESCRIPTOR.message_types_by_name['SafetyStatus']
_SAFETYSTATUS_ITEM = _SAFETYSTATUS.nested_types_by_name['Item']
_SAFETYSTATUS_VALUESENTRY = _SAFETYSTATUS.nested_types_by_name['ValuesEntry']
_SAFETYSTATUSAGGR = DESCRIPTOR.message_types_by_name['SafetyStatusAggr']
_SAFETYDECISION = DESCRIPTOR.message_types_by_name['SafetyDecision']
_SAFETYFAULTREMOVEREQUEST = DESCRIPTOR.message_types_by_name['SafetyFaultRemoveRequest']
_SAFETYFAULTREMOVERESPONSE = DESCRIPTOR.message_types_by_name['SafetyFaultRemoveResponse']
_SAFETYSTATUS_STATUS = _SAFETYSTATUS.enum_types_by_name['Status']
Filter = _reflection.GeneratedProtocolMessageType('Filter', (_message.Message,), {'DESCRIPTOR': _FILTER, '__module__': 'modules.safety_manager_msgs.safety_manager_pb2'})
_sym_db.RegisterMessage(Filter)
SafetyRule = _reflection.GeneratedProtocolMessageType('SafetyRule', (_message.Message,), {'DESCRIPTOR': _SAFETYRULE, '__module__': 'modules.safety_manager_msgs.safety_manager_pb2'})
_sym_db.RegisterMessage(SafetyRule)
Matcher = _reflection.GeneratedProtocolMessageType('Matcher', (_message.Message,), {'DESCRIPTOR': _MATCHER, '__module__': 'modules.safety_manager_msgs.safety_manager_pb2'})
_sym_db.RegisterMessage(Matcher)
RuleMatcher = _reflection.GeneratedProtocolMessageType('RuleMatcher', (_message.Message,), {'DESCRIPTOR': _RULEMATCHER, '__module__': 'modules.safety_manager_msgs.safety_manager_pb2'})
_sym_db.RegisterMessage(RuleMatcher)
RuleMatcherList = _reflection.GeneratedProtocolMessageType('RuleMatcherList', (_message.Message,), {'DESCRIPTOR': _RULEMATCHERLIST, '__module__': 'modules.safety_manager_msgs.safety_manager_pb2'})
_sym_db.RegisterMessage(RuleMatcherList)
SafetyStatus = _reflection.GeneratedProtocolMessageType('SafetyStatus', (_message.Message,), {'Item': _reflection.GeneratedProtocolMessageType('Item', (_message.Message,), {'DESCRIPTOR': _SAFETYSTATUS_ITEM, '__module__': 'modules.safety_manager_msgs.safety_manager_pb2'}), 'ValuesEntry': _reflection.GeneratedProtocolMessageType('ValuesEntry', (_message.Message,), {'DESCRIPTOR': _SAFETYSTATUS_VALUESENTRY, '__module__': 'modules.safety_manager_msgs.safety_manager_pb2'}), 'DESCRIPTOR': _SAFETYSTATUS, '__module__': 'modules.safety_manager_msgs.safety_manager_pb2'})
_sym_db.RegisterMessage(SafetyStatus)
_sym_db.RegisterMessage(SafetyStatus.Item)
_sym_db.RegisterMessage(SafetyStatus.ValuesEntry)
SafetyStatusAggr = _reflection.GeneratedProtocolMessageType('SafetyStatusAggr', (_message.Message,), {'DESCRIPTOR': _SAFETYSTATUSAGGR, '__module__': 'modules.safety_manager_msgs.safety_manager_pb2'})
_sym_db.RegisterMessage(SafetyStatusAggr)
SafetyDecision = _reflection.GeneratedProtocolMessageType('SafetyDecision', (_message.Message,), {'DESCRIPTOR': _SAFETYDECISION, '__module__': 'modules.safety_manager_msgs.safety_manager_pb2'})
_sym_db.RegisterMessage(SafetyDecision)
SafetyFaultRemoveRequest = _reflection.GeneratedProtocolMessageType('SafetyFaultRemoveRequest', (_message.Message,), {'DESCRIPTOR': _SAFETYFAULTREMOVEREQUEST, '__module__': 'modules.safety_manager_msgs.safety_manager_pb2'})
_sym_db.RegisterMessage(SafetyFaultRemoveRequest)
SafetyFaultRemoveResponse = _reflection.GeneratedProtocolMessageType('SafetyFaultRemoveResponse', (_message.Message,), {'DESCRIPTOR': _SAFETYFAULTREMOVERESPONSE, '__module__': 'modules.safety_manager_msgs.safety_manager_pb2'})
_sym_db.RegisterMessage(SafetyFaultRemoveResponse)
if _descriptor._USE_C_DESCRIPTORS == False:
    DESCRIPTOR._options = None
    _SAFETYSTATUS_VALUESENTRY._options = None
    _SAFETYSTATUS_VALUESENTRY._serialized_options = b'8\x01'
    _FILTER._serialized_start = 120
    _FILTER._serialized_end = 175
    _SAFETYRULE._serialized_start = 177
    _SAFETYRULE._serialized_end = 302
    _MATCHER._serialized_start = 304
    _MATCHER._serialized_end = 431
    _RULEMATCHER._serialized_start = 433
    _RULEMATCHER._serialized_end = 544
    _RULEMATCHERLIST._serialized_start = 546
    _RULEMATCHERLIST._serialized_end = 621
    _SAFETYSTATUS._serialized_start = 624
    _SAFETYSTATUS._serialized_end = 1323
    _SAFETYSTATUS_ITEM._serialized_start = 956
    _SAFETYSTATUS_ITEM._serialized_end = 1152
    _SAFETYSTATUS_VALUESENTRY._serialized_start = 1154
    _SAFETYSTATUS_VALUESENTRY._serialized_end = 1199
    _SAFETYSTATUS_STATUS._serialized_start = 1201
    _SAFETYSTATUS_STATUS._serialized_end = 1323
    _SAFETYSTATUSAGGR._serialized_start = 1325
    _SAFETYSTATUSAGGR._serialized_end = 1441
    _SAFETYDECISION._serialized_start = 1443
    _SAFETYDECISION._serialized_end = 1564
    _SAFETYFAULTREMOVEREQUEST._serialized_start = 1566
    _SAFETYFAULTREMOVEREQUEST._serialized_end = 1626
    _SAFETYFAULTREMOVERESPONSE._serialized_start = 1628
    _SAFETYFAULTREMOVERESPONSE._serialized_end = 1689