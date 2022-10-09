from random import choices, randrange
from secrets import choice


def generate_polynom(order: int) -> str:
    polinom = [f'{randrange(2, order)}*x^{order} {choice("+-")}']

    _rand_cuffs = choices([*range(2, order)], k=randrange(1, order))
    _cuffs = [*set(_rand_cuffs)]

    for c in _cuffs[:0:-1]:
        next_part_polling = f'{randrange(1, order)}*x^{c} {choice("+-")}'
        polinom.append(next_part_polling)

    polinom.append(str(_cuffs[0]))
    return f'{" ".join(polinom)} = 0'


with open("poly.txt", "w") as poly:
    for _ in range(3):
        poly.write(generate_polynom(order=int(input())))
        poly.write("\n")

