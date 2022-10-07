import math
n = int(input("input N number: "))


def get_simples(number) -> set[int]:
    bound = int(math.sqrt(number) + 1)
    _temp = {*range(2, bound)}
    for i in range(2, bound):
        powers = set([i * x for x in range(i, bound)])
        _temp -= powers
    return _temp


def get_nodes(number) -> enumerate[int]:
    result = []
    simples = sorted(get_simples(number))
    for simple in simples:
        if number < simple:
            break
        while not number % simple:
            number //= simple
            result.append(simple)
    return result


print(get_nodes(n))

