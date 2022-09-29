real = float(input())

exp: int = len(str(real).split('.')[1])

result = 0
number: int = int(real * 10 ** exp)
while number > 0:
    result += number % 10
    number //= 10

print('digits sum of {} equal {}'.format(real, result))
