import random

n = int(input())
numbers = list(range(n))
print(numbers)


<<<<<<< HEAD
def random_int(seed: int) -> int:
    return int(random.random() * seed)


def shuffle(mass: list) -> enumerate:
    _result = []
    _access_indexes = list(range(n))
    while len(_access_indexes) > 0:
        index = random_int(10)
        if index in _access_indexes:
            _result.append(mass[index])
            _access_indexes.remove(index)

    return _result
=======
def random_int(seed: int) -> int: int(random.random() * seed)


def shuffle(mass: list) -> enumerate:
    result = []
    access_indexes = list(range(n))
    while len(access_indexes) > 0:
        index = int(random.random() * 10)
        if index in access_indexes:
            result.append(numbers[index])
            access_indexes.remove(index)

    return result
>>>>>>> 8b769e35c83271ee2317c9241536ac21c1187fa6


result = shuffle(numbers)
print(result)
<<<<<<< HEAD

=======
>>>>>>> 8b769e35c83271ee2317c9241536ac21c1187fa6
