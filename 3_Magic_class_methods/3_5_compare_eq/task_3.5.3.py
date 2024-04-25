class Track:
    def __init__(self, start_x, start_y):
        self.start_x = start_x
        self.start_y = start_y
        self.tracks = tuple()

    def add_track(self, tr):
        self.tracks += (tr,)

    def get_track(self):
        return self.tracks

    def __call__(self, *args, **kwargs):
        return self.__len__()

    def __len__(self):
        d = 0
        x_1 = self.start_x
        y_1 = self.start_y
        for i in self.tracks:
            x_2, y_2 = i.to_x, i.to_y
            d = int(((x_2 - x_1)**2 + (y_2 - y_1)**2)**0.5)
            d += d
            x_1, y_1 = x_2, y_2
        return d

    @classmethod
    def __verify_data(cls, other):
        if not isinstance(other, int):
            raise TypeError('The right operand must be of type int')

    def __eq__(self, other):
        self.__verify_data(other())
        return self.__len__() == other()

    def __lt__(self, other):
        self.__verify_data(other())
        return self.__len__() < other()


class TrackLine:
    def __init__(self, to_x, to_y, max_speed):
        self.to_x = to_x
        self.to_y = to_y
        self.max_speed = max_speed


track_1 = Track(0, 0)
track_2 = Track(0, 1)
track_1.add_track(TrackLine(2, 4, 100))
track_1.add_track(TrackLine(5, -4, 100))
track_2.add_track(TrackLine(3, 2, 90))
track_2.add_track(TrackLine(10, 8, 90))
print(track_1.get_track(), track_2.get_track(), sep='\n')
print(len(track_1), len(track_2), sep='\n')
print(track_1 == track_2, track_1 != track_2, track_1 > track_2, track_1 < track_2, sep='\n')
