import time


class Mechanical:
    def __init__(self, date):
        self.date = date
        self.name = 'Mechanical'

    def __setattr__(self, key, value):
        if key == 'date' and key in self.__dict__:
            return
        object.__setattr__(self, key, value)


class Aragon:
    def __init__(self, date):
        self.date = date
        self.name = 'Aragon'

    def __setattr__(self, key, value):
        if key == 'date' and key in self.__dict__:
            return
        object.__setattr__(self, key, value)


class Calcium:
    def __init__(self, date):
        self.date = date
        self.name = 'Calcium'

    def __setattr__(self, key, value):
        if key == 'date' and key in self.__dict__:
            return
        object.__setattr__(self, key, value)


class GeyserClassic:
    MAX_DATE_FILTER = 100
    attrs = {'Mechanical': 1, 'Aragon': 2, 'Calcium': 3}

    def __init__(self):
        self.filter_complete_set = [None, None, None]

    def add_filter(self, slot_num, filter):
        if self.filter_complete_set[slot_num - 1] is None and self.attrs[filter.name] == slot_num:
            self.filter_complete_set[slot_num - 1] = filter
        else:
            return 'False'

    def remove_filter(self, slot_num):
        self.filter_complete_set[slot_num - 1] = None

    def get_filters(self):
        return tuple(self.filter_complete_set)

    def water_on(self):
        if None in self.filter_complete_set:
            return False
        return self.check_date(self.filter_complete_set)

    @classmethod
    def check_date(cls, filters):
        for i in filters:
            if 0 > time.time() - i.date or time.time() - i.date > cls.MAX_DATE_FILTER:
                return False
        return True


a = Mechanical(time.time())
print(a.date)
print(a.date - time.time())

my_water = GeyserClassic()
my_water.add_filter(1, Mechanical(time.time()))
my_water.add_filter(2, Aragon(time.time()))
w = my_water.water_on()
print(w)
my_water.add_filter(3, Calcium(time.time()))
w = my_water.water_on()
print(w)
f1, f2, f3 = my_water.get_filters()
print(f1, f2, f3)
print(my_water.add_filter(3, Calcium(time.time())))
print(my_water.add_filter(2, Calcium(time.time())))
