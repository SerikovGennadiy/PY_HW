from enum import Enum


class NumType(Enum):
    No = 0
    Complex = 1
    Real = 2


class Operation(Enum):
    No = 0
    Add = 1
    Sub = 2
    Dev = 4


x = NumType.Complex
print(x.name)
