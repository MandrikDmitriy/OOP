class Track:
    def __init__(self, start_x, start_y):
        self.start_x = start_x
        self.start_y = start_y
        self.track = []

    def add_point(self, x, y, speed):
        self.track.append([(x, y), speed])

    @classmethod
    def __check_index(cls, index, lst):
        if type(index) is not int or index > len(lst) - 1:
            raise IndexError('Index incorrect')

    def __getitem__(self, item):
        self.__check_index(item, self.track)

        return self.track[item]

    def __setitem__(self, key, value):
        self.__check_index(key, self.track)

        self.track[key][1] = value


tr = Track(10, -5.4)
tr.add_point(20, 0, 100)
tr.add_point(50, -20, 80)
tr.add_point(63.45, 1.24, 60.34)
print(tr[2])

tr[2] = 60
c, s = tr[2]
print(c, s)

res = tr[3]
