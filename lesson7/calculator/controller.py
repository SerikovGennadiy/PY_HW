from lesson7.calculator.model.types import NumType, Operation
from lesson7.calculator.ui import show_menu

number_type = NumType.Unset
operation_type = Operation.Unset


def init():
    show_menu()

#
# def preset_num_type():
#     global number_type = NumType(int(input()))
#
#
# def preset_oper_type() -> Operation:
#     return Operation(int(input()))

x = NumType(int(input()))
print(x.name)