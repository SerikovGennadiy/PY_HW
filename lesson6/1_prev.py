import random

n = int(input())


def get_more_than_previos(array: enumerate[int]) -> enumerate[int]:
    return [array[i] for i in range(1, len(array)) if array[i] > array[i - 1]]


rand_list = random.choices(range(n * 10), k=n)
print(rand_list)
print(get_more_than_previos(rand_list))

