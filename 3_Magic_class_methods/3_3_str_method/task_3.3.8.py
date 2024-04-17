class DeltaClick:
    def __init__(self, clock_1, clock_2):
        self.clock_1 = clock_1
        self.clock_2 = clock_2

    def __len__(self):
        diff = self.clock_1.get_time() - self.clock_2.get_time()
        return diff if diff > 0 else 0

    def __str__(self):
        d = self.__len__()
        h = d // 3600
        m = d % 3600 // 60
        s = d % 3600 % 60
        return f'{h:02}:{m:02}:{s:02}'


class Clock:
    def __init__(self, hours, minute, seconds):
        self. hours = hours
        self.minute = minute
        self.seconds = seconds

    def get_time(self):
        return self.hours * 3600 + self.minute * 60 + self.seconds


dt = DeltaClick(Clock(2, 45, 0), Clock(1, 15, 0))
print(dt)
len_dt = len(dt)
print(len_dt)
