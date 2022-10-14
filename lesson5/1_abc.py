import random
import re

n = int(input("Number of words: "))
if n == -1:
    raise Exception("The data is incorrect")

random.seed()
random_list = [''.join(random.choices("абв", k=3)) for word in range(n)]
text = ' '.join(random_list)
print(text)

# try:
# #     print(text.index("абв"))
# # except Exception as e:
# #     print(str(e))

for i, w in enumerate(text.split()):
    if w == "абв":
        print(i, w, w.__eq__("абв"))

# print(text := text.replace("абв", ""))

# result = ' '.join(list(filter(lambda word: not word.__eq__("абв"), text.split())))
# print(result)

print(result := re.sub("\s?абв\s?", "", text))
