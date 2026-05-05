"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
_sym_db = _symbol_database.Default()
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\nPmodules/planning/tasks/path_reference_decider/proto/path_reference_decider.proto\x12\x0fapollo.planning"\xcb\x01\n\x1aPathReferenceDeciderConfig\x12%\n\x19min_path_reference_length\x18\x01 \x01(\r:\x0220\x12#\n\x1bweight_x_ref_path_reference\x18\x02 \x01(\x01\x12/\n skip_path_reference_in_side_pass\x18\x03 \x01(\x08:\x05false\x120\n"skip_path_reference_in_change_lane\x18\x04 \x01(\x08:\x04true')
_PATHREFERENCEDECIDERCONFIG = DESCRIPTOR.message_types_by_name['PathReferenceDeciderConfig']
PathReferenceDeciderConfig = _reflection.GeneratedProtocolMessageType('PathReferenceDeciderConfig', (_message.Message,), {'DESCRIPTOR': _PATHREFERENCEDECIDERCONFIG, '__module__': 'modules.planning.tasks.path_reference_decider.proto.path_reference_decider_pb2'})
_sym_db.RegisterMessage(PathReferenceDeciderConfig)
if _descriptor._USE_C_DESCRIPTORS == False:
    DESCRIPTOR._options = None
    _PATHREFERENCEDECIDERCONFIG._serialized_start = 102
    _PATHREFERENCEDECIDERCONFIG._serialized_end = 305