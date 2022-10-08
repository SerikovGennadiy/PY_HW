from random import choices
from itertools import groupby

n = int(input())
if n == -1:
    raise Exception("Negative value of the number of numbers!")

rand_list = sorted(choices([*range(1, n)], k=n))
# dict_list = dict.fromkeys(rand_list, 1)
# print(dict_list)
result_list = [num for num, gr in groupby(rand_list) if len(list(gr)) == 1]

print(rand_list)
print(result_list)


