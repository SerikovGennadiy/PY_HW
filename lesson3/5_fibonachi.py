n = int(input())

positive_part = [0]
negative_part = []

i = 0
negative_part.append(i)

j = 1
positive_part.append(j)
negative_part.append(j)

for p in range(n):
    k = i + j
    positive_part.append(k)
    print(-1 ** p)
    negative_part.append(k * (-1 ** p))
    i = j
    j = k

print(positive_part)
print(negative_part)
