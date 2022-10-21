from lesson7.calculator import ui
from lesson7.calculator.model.calculator import make_calculation
from lesson7.calculator.model.types import NumType, Operation
from lesson7.calculator.repo import log

number_type = NumType.Unset
operation_type = Operation.Unset


def init():
    ui.show_menu()


def start():
    while True:
        q = input('Quit ? (yes/no): ')
        if q.startswith('y'):
            log.show_log()
            return
        try:
            _presetup_calc()
            operands = _get_operands()
            result = make_calculation(operation_type, operands)
            log.write_log(operation_type, operands, result)
            show_result(operands, result)
        except Exception as exp:
            print(str(exp))


def show_result(operands, result):
    ui.show_result(f'{operation_type.name} of {operands[0]} and {operands[1]} is equal {result}')


def _get_operands() -> (object, object):
    match number_type:
        case NumType.Complex:
            try:
                real_first, image_first = \
                    float(input("insert first real part: ")), \
                    float(input("insert first image part: "))
                real_second, image_second = \
                    float(input("insert second real part: ")), \
                    float(input("insert second image part: "))
            except BaseException:
                raise Exception("error during get complex operands!")
            return complex(real_first, image_first), complex(real_second, image_second)
        case NumType.Real:
            try:
                first = float(input("insert first number: "))
                second = float(input("insert second number: "))
            except BaseException:
                raise Exception("error during get real operands!")
            return first, second


def _presetup_calc():
    _choice_num_type()
    _choice_operation()


def _choice_num_type():
    global number_type
    try:
        number_type = NumType(int(input('Insert number type: ')))
    except BaseException:
        raise Exception('error during selecting number type!')


def _choice_operation():
    global operation_type
    try:
        operation_type = Operation(int(input('Insert operation type: ')))
    except BaseException:
        raise Exception('error during selecting operation type!')
