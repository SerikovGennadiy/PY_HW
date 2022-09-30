pos1 = int(input("Position one: ")) - 1
pos2 = int(input("Position two: ")) - 1

n = int(input("Number of elements: "))

if n < pos1 < pos2:
    raise Exception("array size less than positions")

numbers = list(range(-n, n + 1))

print(numbers)
print(f'{numbers[pos1] * numbers[pos2]}')
