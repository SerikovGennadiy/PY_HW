from lesson7.calculator.model.types import NumType, Operation
from lesson7.calculator.ui import show_menu

number_type = NumType.Unset
operation_type = Operation.Unset


def init():
    show_menu()


def choice_num_type():
    global number_type
    number_type = NumType(int(input()))


def choice_operation():
    global operation_type
    operation_type = Operation(int(input()))
