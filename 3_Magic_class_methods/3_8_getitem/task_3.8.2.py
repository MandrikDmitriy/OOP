class Record:
    def __init__(self, **kwargs):
        self.field_name = []
        for key, val in kwargs.items():
            self.__dict__[key] = val
            self.field_name.append(key)

    @classmethod
    def check_index(cls, val, length):
        if type(val) is not int or length - 1 < val:
            raise IndexError('Index incorrect')

    def __getitem__(self, item):
        self.check_index(item, len(self.field_name))

        return self.__dict__[self.field_name[item]]

    def __setitem__(self, key, value):
        self.check_index(key, len(self.field_name))
        self.__dict__[self.field_name[key]] = value


rec = Record(pk=1, title='Python OOP', author='Un name')
rec[0] = 2
rec[1] = "super course"
rec[2] = 'BCM'
print(rec[1])
# rec[3]
        