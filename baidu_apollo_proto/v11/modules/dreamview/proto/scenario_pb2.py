"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
_sym_db = _symbol_database.Default()
from ....modules.common_msgs.simulation_msgs import scenario_pb2 as modules_dot_common__msgs_dot_simulation__msgs_dot_scenario__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n&modules/dreamview/proto/scenario.proto\x12\x10apollo.dreamview\x1a2modules/common_msgs/simulation_msgs/scenario.proto"\xae\x02\n\tSimTicket\x12\n\n\x02id\x18\x01 \x01(\t\x12\x13\n\x0bauthor_name\x18\x02 \x01(\t\x12-\n\x08scenario\x18\x03 \x01(\x0b2\x1b.apollo.simulation.Scenario\x12\x0c\n\x04type\x18\x04 \x01(\t\x12\x0e\n\x06map_id\x18\x05 \x01(\t\x12\x11\n\tblob_path\x18\x06 \x01(\t\x12\x0c\n\x04tags\x18\x07 \x03(\t\x12\x10\n\x08category\x18\x08 \x01(\t\x12\x0c\n\x04time\x18\t \x01(\t\x12\x13\n\x0bcreate_time\x18\n \x01(\t\x12\x0e\n\x06number\x18\x0b \x01(\x05\x12\x16\n\x0edescription_cn\x18\x0c \x01(\t\x12\x16\n\x0edescription_en\x18\r \x01(\t\x12\x1d\n\x15description_en_tokens\x18\x0e \x03(\t"\x82\x02\n\x0cUserAdsGroup\x12\n\n\x02id\x18\x01 \x01(\t\x12\x0c\n\x04name\x18\x02 \x01(\t\x12\x0e\n\x06userid\x18\x03 \x01(\t\x12\x11\n\tticketids\x18\x04 \x03(\t\x12#\n\x1bvisible_to_privileged_users\x18\x05 \x01(\x08\x12\x0c\n\x04type\x18\x06 \x01(\t\x12\x0c\n\x04tags\x18\x07 \x03(\t\x12\x14\n\x0cdescripition\x18\x08 \x01(\t\x12\x13\n\x0bcreate_time\x18\t \x01(\x01\x12\x10\n\x08mod_time\x18\n \x01(\x01\x12\x10\n\x08category\x18\x0b \x01(\t\x12\x11\n\tis_public\x18\x0c \x01(\x08\x12\x12\n\nis_classic\x18\r \x01(\x08')
_SIMTICKET = DESCRIPTOR.message_types_by_name['SimTicket']
_USERADSGROUP = DESCRIPTOR.message_types_by_name['UserAdsGroup']
SimTicket = _reflection.GeneratedProtocolMessageType('SimTicket', (_message.Message,), {'DESCRIPTOR': _SIMTICKET, '__module__': 'modules.dreamview.proto.scenario_pb2'})
_sym_db.RegisterMessage(SimTicket)
UserAdsGroup = _reflection.GeneratedProtocolMessageType('UserAdsGroup', (_message.Message,), {'DESCRIPTOR': _USERADSGROUP, '__module__': 'modules.dreamview.proto.scenario_pb2'})
_sym_db.RegisterMessage(UserAdsGroup)
if _descriptor._USE_C_DESCRIPTORS == False:
    DESCRIPTOR._options = None
    _SIMTICKET._serialized_start = 113
    _SIMTICKET._serialized_end = 415
    _USERADSGROUP._serialized_start = 418
    _USERADSGROUP._serialized_end = 676