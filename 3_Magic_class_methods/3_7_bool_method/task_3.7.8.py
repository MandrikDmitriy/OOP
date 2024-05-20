from random import randint


class GamePole:
    __instance = None

    def __new__(cls, *args, **kwargs):
        if cls.__instance is None:
            cls.__instance = super().__new__(cls)
        return cls.__instance

    def __del__(self):
        self.__instance = None

    def __init__(self, n, m, total_mines):
        self._n = n
        self._m = m
        self.total_mines = total_mines
        self.__pole_cells = tuple(tuple(Cell() for _ in range(self._m))
                                  for _ in range(self._n))
        self.init_pole()

    @property
    def pole(self):
        return self.__pole_cells

    def init_pole(self):
        for c in self.__pole_cells:
            for f in c:
                f.is_open = False
                f.is_mine = False

        count_mines = self.total_mines
        while count_mines > 0:
            i = randint(0, self._n - 1)
            j = randint(0, self._m - 1)
            if self.__pole_cells[i][j].is_mine is False:
                self.__pole_cells[i][j].is_mine = True
                count_mines -= 1

        ind = (-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)

        for x in range(self._n):
            for y in range(self._m):
                if self.__pole_cells[x][y].is_mine is False:
                    mines = sum((self.pole[x+i][y+j].is_mine for i, j in ind if 0 <= x + i < self._n and 0 <= y + j < self._m))
                    self.__pole_cells[x][y].number = mines

    def open_cell(self, i, j):
        if i > self._n or j > self._m:
            raise IndexError('Index incorrect')
        else:
            self.__pole_cells[i][j].is_open = True

    def show_pole(self):
        for j in self.pole:
            print(*map(lambda x: '#' if not x.is_open else ('*' if x.is_mine else x.number), j))

    def show_oll_pole(self):
        for p in self.__pole_cells:
            for k in p:
                k.is_open = True
        self.show_pole()


class CellValue:
    @classmethod
    def verify_cell(cls, val):
        if 0 > val > 8:
            raise ValueError('Incorrect attribute')

    def __set_name__(self, owner, name):
        self.name = '_' + name

    def __get__(self, instance, owner):
        return getattr(instance, self.name)

    def __set__(self, instance, value):
        self.verify_cell(value)
        setattr(instance, self.name, value)


class Cell:
    is_mine = CellValue()
    number = CellValue()
    is_open = CellValue()

    def __init__(self):
        self.is_mine = False
        self.number = 0
        self.is_open = False

    def __bool__(self):
        return not self.is_open


pole = GamePole(3, 5, 4)
pole.show_oll_pole()
