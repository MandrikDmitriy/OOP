class FloatValue:
    @classmethod
    def verify_float(cls, value):
        if type(value) is not float:
            raise TypeError('You can assign only float data type')

    def __set_name__(self, owner, name):
        self.name = '_' + name

    def __get__(self, instance, owner):
        return getattr(instance, self.name)

    def __set__(self, instance, value):
        self.verify_float(value)
        setattr(instance, self.name, value)


class Cell:
    value = FloatValue()

    def __init__(self, val=0.0):
        self.value = val


class TableSheet:
    def __init__(self, n, m):
        self.cells = [[Cell() for _ in range(m)] for _ in range(n)]


N = 5
M = 3
table = TableSheet(N, M)
num = 1.0
for i in range(N):
    for k in range(M):
        table.cells[i][k].value = num
        num += 1
for i in range(N):
    for k in range(M):
        print(table.cells[i][k].value)
print(table.cells)
