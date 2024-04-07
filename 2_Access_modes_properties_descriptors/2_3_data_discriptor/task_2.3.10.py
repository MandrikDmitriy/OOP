class TVProgram:
    def __init__(self, name_channel):
        self.name_channel = name_channel
        self.items = []

    def add_telecast(self, tl):
        self.items.append(tl)

    def remove_telecast(self, indx):
        # t_lst = tuple(filter(lambda x: x.uid == indx, self.items))
        # for t in t_lst:
        #   self.items.remove(t)
        for ind, val in enumerate(self.items):
            if val.uid == indx:
                self.items.pop(ind)


class Telecast:
    def __init__(self, uid, name, duration):
        self.__id = uid
        self.__name = name
        self.__duration = duration

    @property
    def uid(self):
        return self.__id

    @uid.setter
    def uid(self, uid):
        self.__id = uid

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name):
        self.__name = name

    @property
    def duration(self):
        return self.__duration

    @duration.setter
    def duration(self, duration):
        self.__duration = duration


pr = TVProgram('First channel')
pr.add_telecast(Telecast(1, 'Good morning', 10000))
pr.add_telecast(Telecast(2, 'News', 2000))
pr.add_telecast(Telecast(3, 'Interview with you', 20))
pr.remove_telecast(2)
for i in pr.items:
    print(f'{i.uid}: {i.name} - {i.duration}')
