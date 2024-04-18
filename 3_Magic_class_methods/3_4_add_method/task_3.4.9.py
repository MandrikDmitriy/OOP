class Box3D:
    def __init__(self, width, height, depth):
        self.width = width
        self.height = height
        self.depth = depth

    def get_val(self):
        return self.width, self.height, self.depth

    def __add__(self, other):
        w = self.width + other.width
        h = self.height + other.height
        d = self.depth + other.depth
        return Box3D(w, h, d)

    def __sub__(self, other):
        w = self.width - other.width
        h = self.height - other.height
        d = self.depth - other.depth
        return Box3D(w, h, d)

    def __mul__(self, other):
        w = self.width * other
        h = self.height * other
        d = self.depth * other
        return Box3D(w, h, d)

    def __rmul__(self, other):
        return self.__mul__(other)

    def __floordiv__(self, other):
        w = self.width // other
        h = self.height // other
        d = self.depth // other
        return Box3D(w, h, d)

    def __mod__(self, other):
        w = self.width % other
        h = self.height % other
        d = self.depth % other
        return Box3D(w, h, d)


box_1 = Box3D(1, 2, 3)
box_2 = Box3D(2, 4, 6)
box = box_1 + box_2
print(box.get_val())
box = box_1 * 2
print(box.get_val())
box = 3 * box_2
print(box.get_val())
box = box_2 - box_1
print(box.get_val())
box = box_1 // 2
print(box.get_val())
box = box_2 % 3
print(box.get_val())
