from lesson7.calculator.model.types import Operation


def make_calculation(operation_type: Operation, operands) -> object:
    result = None
    a, b = operands
    match operation_type:
        case Operation.Addition:
            result = a + b
        case Operation.Subtraction:
            result = a - b
        case Operation.Multiply:
            result = a * b
        case Operation.Division:
            result = a / b

    return result
