from random import uniform


def min_max(floats: enumerate[float]) -> (float, float):
    _min, _max = 0, 0
    for _n in floats:
        _min = _n if _n < _min else _min
        _max = _n if _n > _max else _max
    return _min, _max


n = int(input("insert n: "))

nums = [round(uniform(-10, 10), 2) for i in range(n)]
min_max_values = min_max(nums)

print(nums)
print('Min: {0} \t Max:{1} \t Difference:{2}'.format(
        min_max_values[0],
        min_max_values[1],
        round(min_max_values[1] - min_max_values[0], 2)))
