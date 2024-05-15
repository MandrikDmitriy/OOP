class DataBase:
    dict_db = {}

    def __init__(self, path):
        self.path = path

    def write(self, record):
        if record in self.dict_db:
            self.dict_db[record].append(record)
        else:
            self.dict_db[record] = [record]

    def read(self, pk):
        for key, val in self.dict_db.items():
            for i in val:
                if i.pk == pk:
                    return i
        raise ValueError('Value not found')


class Record:
    __count = 0

    def __new__(cls, *args, **kwargs):
        cls.__count += 1
        return super().__new__(cls)

    def __init__(self, fio, descr, old):
        self.pk = self.__count
        self.fio = fio
        self.descr = descr
        self.old = old

    def __hash__(self):
        return hash((self.fio.lower(), self.old))

    def __eq__(self, other):
        return hash(self) == hash(other)


with open('task_3.6.7.txt', 'r', encoding='utf-8') as file:
    lst_in = list(x.split('; ') for x in file.read().splitlines())

print(lst_in)
db = DataBase('c:data_base')
for obj in lst_in:
    db.write(Record(*obj))
print(db.dict_db)
print(db.read(5))
