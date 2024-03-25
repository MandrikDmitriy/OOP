class Clock:
    def __init__(self, tm=0):
        self.__time = 0
        if self.__check_time(tm):
            self.__time = tm

    @classmethod
    def __check_time(cls, tm):
        return type(tm) == int and 0 <= tm < 100000

    def set_time(self, tm):
        if self.__check_time(tm):
            self.__time = tm

    def get_time(self):
        return self.__time


clock = Clock(4530)
print(clock.get_time())