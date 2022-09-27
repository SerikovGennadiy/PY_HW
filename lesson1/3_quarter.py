def show_quarter(x: int, y: int) -> object:
    if x > 0 and y > 0:
        return 1
    elif x < 0 and y > 0:
        return 2
    elif x < 0 and y < 0:
        return 3
    elif x > 0 and y < 0:
        return 4


x: int = int(input("insert x: "))
y: int = int(input("insert y: "))

print(f"we've got {show_quarter(x, y)} quarter")
