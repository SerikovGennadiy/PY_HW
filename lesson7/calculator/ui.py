def _menu() -> str:
    intro = 'Calculator complex and real numbers'
    settings = f'Number types: \n' \
               f'\tComplex\t - 1\n' \
               f'\t{"Real":>7}\t - 2' \
               f'\n\nOperations: \n' \
               f'\t{"Addition":>11}\t- 1\n' \
               f'\t{"Subtraction":>11}\t- 2\n' \
               f'\t{"Multiply":>11}\t- 3\n' \
               f'\t{"Division":>11}\t- 4\n'

    return f'{intro}\n{settings}'


def show_menu():
    print(_menu())


def show_result(result):
    print(result)
