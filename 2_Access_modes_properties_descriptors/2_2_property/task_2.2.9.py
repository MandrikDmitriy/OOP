class LineTo:
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y


class PathLine:
    def __init__(self, *args):
        self.coords = list((LineTo(0, 0),) + args)

    def get_path(self):
        return self.coords[1:]

    def add_line(self, line):
        self.coords.append(line)

    def get_length(self):
        f = ((self.coords[i - 1], self.coords[i]) for i in range(1, len(self.coords)))
        return sum(map(lambda t: ((t[0].x - t[1].x) ** 2 + (t[0].y - t[1].y) ** 2) ** 0.5, f))


p = PathLine(LineTo(10, 20), LineTo(10, 30))
p.add_line(LineTo(20, -10))
p.add_line(LineTo(20, -30))
print(p.get_path())
print(p.get_length())