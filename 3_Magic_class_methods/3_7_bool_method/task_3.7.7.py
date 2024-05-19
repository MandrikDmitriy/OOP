class Ellipse:
    def __init__(self, x1=0, x2=0, y1=0, y2=0):
        self.x1 = x1
        self.x2 = x2
        self.y1 = y1
        self.y2 = y2

    def __bool__(self):
        return any((self.x1, self.x2, self.y1, self.y2))

    def get_coords(self):
        if not bool(self):
            raise AttributeError('Coordinates isn\'t')
        return self.x1, self.x2, self.y1, self.y2


el_1 = Ellipse()
el_2 = Ellipse(1, 2, 3, 4)
el_3 = Ellipse()
el_4 = Ellipse(5, 6, 7, 8)
lst_geom = [el_1, el_2, el_3, el_4]
for i in lst_geom:
    if bool(i):
        print(i.get_coords())
