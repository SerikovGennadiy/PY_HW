n = int(input("insert position's amount: "))

i = 0
positive_part = [i]

j = 1
positive_part.append(j)
negative_part = [j]

for p in range(1, n + 1):
    k = i + j
    positive_part.append(k)
    negative_part.append(k * ((-1) ** p))
    i = j
    j = k

result = [*negative_part[::-1], *positive_part]
print(result)
