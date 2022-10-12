import itertools

# full_names_input = input("insert full names e.g: Иван Сергеев, Инна Серова, Петр Алексеев : ")
full_names_input = "Иван Сергеев, Инна Серова, Петр Алексеев, Илья Иванов, Анна Савельева, Юнона Ветрякова, Борис Аркадьев, Антон Серов, Павел Анисимов"
full_names = sorted(full_names_input.split(", "),
                    key=lambda fn: fn.split()[1][0])
# print(full_names)

full_names_by_last_name = dict([(n, list(k)) for n, k in
                                itertools.groupby(full_names, key=lambda n: n.split()[1][0])])
# print(full_names_by_last_name)

for n in full_names_by_last_name:
    full_names_by_last_name[n] = dict([(x, list(y)) for x, y in
                                  itertools.groupby(sorted(full_names_by_last_name[n]), key=lambda x: x[0])])

print(full_names_by_last_name)