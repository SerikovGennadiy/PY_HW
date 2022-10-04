from random import sample

n = int(input("insert n: "))
nums = sample(range(n), k=n)
print(nums)

size = len(nums)
result = []

bound = size // 2
for i in range(bound):
    result.append(nums[i] * nums[-i - 1])

is_nums_not_even = not size % 2 == 0
if is_nums_not_even:
    result.append(nums[bound])

print(result)