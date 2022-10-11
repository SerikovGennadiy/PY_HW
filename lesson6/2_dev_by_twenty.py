n = int(input("insert number: "))

mass = [*range(1, n+1)]
devided_by_twenties = [n for n in mass if n % 20 == 0 or n % 21 == 0]

print(devided_by_twenties)

