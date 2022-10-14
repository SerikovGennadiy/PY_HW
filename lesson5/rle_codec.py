from itertools import groupby


def encrypt_rle(text: str) -> str:
    _temp = [f'{len(list(k))}{ch}' for ch, k in groupby(text, key=lambda ch: ch)]
    return ''.join(_temp)


def decrypt_rle(coded: str) -> str:
    result = []
    index = 0
    for i, c in enumerate(coded):
        if not c.isdigit():
            result.append(f'{c * int(coded[index:i])}')
            index = i + 1
    return ''.join(result)
