class PolyLine:
    def __init__(self, *args):
        self.coords = list(args)

    def add_coord(self, x, y):
        self.coords.append((x, y))

    def remove_coord(self, indx):
        self.coords.pop(indx)

    def get_coords(self):
        return self.coords


poly = PolyLine((1, 2), (3, 4), (1, 10), (4, 20))
poly.add_coord(5, 8)
poly.remove_coord(1)
res = poly.get_coords()
print(res)
