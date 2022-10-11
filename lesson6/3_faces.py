import re
import itertools

names_input = input("insert person's names, e.g Ivan, Petr, Sidor : ")

names = sorted(list(map(lambda x: x.strip(), re.split(",", names_input))))
faces = [(x, list(y)) for x, y in itertools.groupby(names, key=lambda x: x[0])]
print(dict(faces))