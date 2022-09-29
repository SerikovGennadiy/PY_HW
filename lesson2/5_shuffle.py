import random

n = int(input())
numbers = list(range(n))
print(numbers)


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


result = shuffle(numbers)
print(result)
