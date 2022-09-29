num = int(input())

numbers = [round((1 + 1 / i) ** i) for i in range(1, num + 1)]
print(numbers)
