from os import path
from lesson5.rle_codec import encrypt_rle, decrypt_rle

# source_file = "text_words.txt"
# coded_file = "text_code_words.txt"

source_file = input("Enter the name of the file with the text : ")
coded_file = input("Enter the file name to record : ")


if path.exists(source_file) and \
        path.exists(coded_file):
    with open(source_file, 'r') as source, \
            open(coded_file, 'w') as file:
        print(source.name)
        while line := source.readline().rstrip():
            print(line)
            file.write(f'{encrypt_rle(line)}\n')

    with open(coded_file, 'r') as file:
        print(file.name)
        while line := file.readline().rstrip():
            print(f'RLE coded: {line}')
            print(f'RLE decoded: {decrypt_rle(line)}')

else:
    raise Exception("that files don't exist")
