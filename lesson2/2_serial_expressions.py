number = int(input())


def fact(n: int) -> int:
    if n <= 1:
        return 1
    return n * fact(n - 1)


result = [fact(i) for i in range(1, number + 1)]
print(result)
