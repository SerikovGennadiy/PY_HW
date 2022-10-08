r = float(input("Enter the real number : "))
a = len((input("Enter the required accuracy '0.0001': ")).split('.')[1])

print(f'{r:.{a}f}')

