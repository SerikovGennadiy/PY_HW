from lesson7.calculator.model.types import Operation
from lesson7.calculator.utils.utils import _datetime_stamp as stamp

calculator_log = []


def write_log(operation: Operation, operands: (object, object), result: object):
    calculator_log.append({
        'datetime': stamp(),
        'operation': operation.name,
        'message': f'{operation.name} of {operands[0]} and {operands[1]} is equal {result}'
    })


def show_log():
    for record in calculator_log:
        print(record)
