from enum import Enum


class NumType(Enum):
    Unset = 0
    Complex = 1
    Real = 2


class Operation(Enum):
    Unset = 0
    Addition = 1
    Subtraction = 2
    Multiply = 3
    Division = 4
