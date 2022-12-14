import random

n = int(input())
numbers = list(range(n))
print(numbers)


def random_int(seed: int) -> int:
    return int(random.random() * seed)


def shuffle(mass: list) -> enumerate:
    _size = len(mass)
    _result = []
    _access_indexes = list(range(_size))
    while len(_access_indexes) > 0:
        index = random_int(_size)
        if index in _access_indexes:
            _result.append(mass[index])
            _access_indexes.remove(index)

    return _result


result = shuffle(numbers)
print(result)
