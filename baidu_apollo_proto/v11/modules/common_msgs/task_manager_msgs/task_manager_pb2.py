"""Generated protocol buffer code."""
from google.protobuf.internal import enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
_sym_db = _symbol_database.Default()
from ....modules.common_msgs.basic_msgs import header_pb2 as modules_dot_common__msgs_dot_basic__msgs_dot_header__pb2
from ....modules.common_msgs.routing_msgs import routing_pb2 as modules_dot_common__msgs_dot_routing__msgs_dot_routing__pb2
from ....modules.common_msgs.external_command_msgs import lane_follow_command_pb2 as modules_dot_common__msgs_dot_external__command__msgs_dot_lane__follow__command__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n8modules/common_msgs/task_manager_msgs/task_manager.proto\x12\x13apollo.task_manager\x1a+modules/common_msgs/basic_msgs/header.proto\x1a.modules/common_msgs/routing_msgs/routing.proto\x1aCmodules/common_msgs/external_command_msgs/lane_follow_command.proto"n\n\x10CycleRoutingTask\x12\x11\n\tcycle_num\x18\x01 \x01(\x05\x12G\n\x13lane_follow_command\x18\x02 \x01(\x0b2*.apollo.external_command.LaneFollowCommand"a\n\x12ParkingRoutingTask\x12\x12\n\nlane_width\x18\x01 \x01(\x01\x127\n\x0frouting_request\x18\x02 \x01(\x0b2\x1e.apollo.routing.RoutingRequest"_\n\x11ParkGoRoutingTask\x12\x11\n\tpark_time\x18\x01 \x01(\x05\x127\n\x0frouting_request\x18\x02 \x01(\x0b2\x1e.apollo.routing.RoutingRequest"\xc2\x02\n\x04Task\x12%\n\x06header\x18\x01 \x01(\x0b2\x15.apollo.common.Header\x12\x11\n\ttask_name\x18\x02 \x01(\t\x120\n\ttask_type\x18\x03 \x01(\x0e2\x1d.apollo.task_manager.TaskType\x12A\n\x12cycle_routing_task\x18\x04 \x01(\x0b2%.apollo.task_manager.CycleRoutingTask\x12E\n\x14parking_routing_task\x18\x05 \x01(\x0b2\'.apollo.task_manager.ParkingRoutingTask\x12D\n\x14park_go_routing_task\x18\x06 \x01(\x0b2&.apollo.task_manager.ParkGoRoutingTask*G\n\x08TaskType\x12\x11\n\rCYCLE_ROUTING\x10\x00\x12\x13\n\x0fPARKING_ROUTING\x10\x01\x12\x13\n\x0fPARK_GO_ROUTING\x10\x02*V\n\x0cJunctionType\x12\x0b\n\x07UNKNOWN\x10\x00\x12\x0b\n\x07IN_ROAD\x10\x01\x12\x0e\n\nCROSS_ROAD\x10\x02\x12\r\n\tFORK_ROAD\x10\x03\x12\r\n\tMAIN_SIDE\x10\x04')
_TASKTYPE = DESCRIPTOR.enum_types_by_name['TaskType']
TaskType = enum_type_wrapper.EnumTypeWrapper(_TASKTYPE)
_JUNCTIONTYPE = DESCRIPTOR.enum_types_by_name['JunctionType']
JunctionType = enum_type_wrapper.EnumTypeWrapper(_JUNCTIONTYPE)
CYCLE_ROUTING = 0
PARKING_ROUTING = 1
PARK_GO_ROUTING = 2
UNKNOWN = 0
IN_ROAD = 1
CROSS_ROAD = 2
FORK_ROAD = 3
MAIN_SIDE = 4
_CYCLEROUTINGTASK = DESCRIPTOR.message_types_by_name['CycleRoutingTask']
_PARKINGROUTINGTASK = DESCRIPTOR.message_types_by_name['ParkingRoutingTask']
_PARKGOROUTINGTASK = DESCRIPTOR.message_types_by_name['ParkGoRoutingTask']
_TASK = DESCRIPTOR.message_types_by_name['Task']
CycleRoutingTask = _reflection.GeneratedProtocolMessageType('CycleRoutingTask', (_message.Message,), {'DESCRIPTOR': _CYCLEROUTINGTASK, '__module__': 'modules.common_msgs.task_manager_msgs.task_manager_pb2'})
_sym_db.RegisterMessage(CycleRoutingTask)
ParkingRoutingTask = _reflection.GeneratedProtocolMessageType('ParkingRoutingTask', (_message.Message,), {'DESCRIPTOR': _PARKINGROUTINGTASK, '__module__': 'modules.common_msgs.task_manager_msgs.task_manager_pb2'})
_sym_db.RegisterMessage(ParkingRoutingTask)
ParkGoRoutingTask = _reflection.GeneratedProtocolMessageType('ParkGoRoutingTask', (_message.Message,), {'DESCRIPTOR': _PARKGOROUTINGTASK, '__module__': 'modules.common_msgs.task_manager_msgs.task_manager_pb2'})
_sym_db.RegisterMessage(ParkGoRoutingTask)
Task = _reflection.GeneratedProtocolMessageType('Task', (_message.Message,), {'DESCRIPTOR': _TASK, '__module__': 'modules.common_msgs.task_manager_msgs.task_manager_pb2'})
_sym_db.RegisterMessage(Task)
if _descriptor._USE_C_DESCRIPTORS == False:
    DESCRIPTOR._options = None
    _TASKTYPE._serialized_start = 876
    _TASKTYPE._serialized_end = 947
    _JUNCTIONTYPE._serialized_start = 949
    _JUNCTIONTYPE._serialized_end = 1035
    _CYCLEROUTINGTASK._serialized_start = 243
    _CYCLEROUTINGTASK._serialized_end = 353
    _PARKINGROUTINGTASK._serialized_start = 355
    _PARKINGROUTINGTASK._serialized_end = 452
    _PARKGOROUTINGTASK._serialized_start = 454
    _PARKGOROUTINGTASK._serialized_end = 549
    _TASK._serialized_start = 552
    _TASK._serialized_end = 874