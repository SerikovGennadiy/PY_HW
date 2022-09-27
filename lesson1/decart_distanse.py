def get_distanse(x1: int, y1: int, x2: int, y2: int) -> float:
    return round((((x2 - x1) ** 2) + ((y2 - y1) ** 2)) ** 0.5, 3)


x1 = int(input("insert x1: "))
x2 = int(input("insert x2: "))
y1 = int(input("insert y1: "))
y2 = int(input("insert y2: "))

print(get_distanse(x1, x2, y1, y2))
