from typing import Any

field: list[Any] = [[''] * 3 for _ in range(3)]


def init(new_field):
    global field
    field = new_field[:]


def show():
    print('\t ', end='')
    for i in range(3):
        print(f'{i + 1}\t', end='\t')
    print("\n")

    for i in range(3):
        print(f'{i + 1}\t ', end='')
        for j in range(3):
            print(f'{field[i][j]}\t\t', end='')
        print('\n')


def set_cell(i, j, mark):
    field[i][j] = mark


def move(i, j, mark):
    if can_player_move(i - 1, j - 1, mark):
        set_cell(i - 1, j - 1, mark)


def can_player_move(i, j, mark):
    return mark_correct(mark) and is_cell_empty(i, j) and range_correct(i, j)


def mark_correct(mark):
    return check_cell_by(lambda: mark == 'O' or mark == 'X',
                         "use only X or Y marks!")


def is_cell_empty(i, j):
    return check_cell_by(lambda: field[i][j] not in ['X', 'O'],
                         "cell is busy!")


def range_correct(i, j):
    return check_cell_by(lambda: 0 <= i <= 2 and 0 <= j <= 2,
                         "choose correct cells' indexes for step [0,2] and marks X or O")


def check_cell_by(func, message):
    is_correct = func()
    if not is_correct:
        print(message)
    return is_correct
