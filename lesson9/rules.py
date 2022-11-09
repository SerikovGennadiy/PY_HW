class Player(object):
    def __init__(self):
        self._name = None
        self._mark = None

    def info(self):
        return f'Player {self._name} goes by {self._mark}'

    def set_name(self, name):
        self._name = name
        return self

    def get_name(self):
        return self._name

    def set_mark(self, mark):
        self._mark = mark
        return self


def check_vin(field: list) -> (bool, str):
    for _x in range(3):
        if field[_x][0] == field[_x][1] == field[_x][2] and field[_x][0] in ["X", "O"]:
            return True, field[_x][0]
        if field[0][_x] == field[1][_x] == field[2][_x] and field[0][_x] in ["X", "O"]:
            return True, field[0][_x]
    if field[0][0] == field[1][1] == field[2][2] and field[0][0] in ["X", "O"]:
        return True, field[0][0]
    if field[2][0] == field[1][1] == field[0][2] and field[2][0] in ["X", "O"]:
        return True, field[2][0]


player = Player()
player\
    .set_name('Ronaldo')\
    .set_mark("X")
print(player.info())
