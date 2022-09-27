# ¬(X ⋁ Y ⋁ Z) = ¬X ⋀ ¬Y ⋀ ¬Z

predicate  = lambda x, y, z: not (x or y or z) == (not x and not y and not z)

print(f'test predicate ¬(X ⋁ Y ⋁ Z) = ¬X ⋀ ¬Y ⋀ ¬Z\n')

for i in range(2):
    for j in range(2):
        for k in range(2):
            print(f'{i} {j} {k} -> {predicate(i, j, k)}')
