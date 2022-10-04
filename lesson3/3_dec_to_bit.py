dec = int(input("insert int number: "))

bit = 1
bit_view = []
while dec > bit:
    bit_view.append("1" if dec & bit != 0 else "0")
    bit <<= 1

print(''.join(bit_view))