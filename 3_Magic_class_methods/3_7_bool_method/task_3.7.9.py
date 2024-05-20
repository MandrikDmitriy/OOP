class Vector:
    def __init__(self, *args):
        self.coords = args

    @classmethod
    def get_sum(cls, obj_1, obj_2):
        return tuple(obj_1[x] + obj_2[x] for x in range(len(obj_1)))

    @classmethod
    def get_dif(cls, obj_1, obj_2):
        return tuple(obj_1[x] - obj_2[x] for x in range(len(obj_1)))

    @classmethod
    def get_mult(cls, obj_1, obj_2):
        return tuple(obj_1[x] * obj_2[x] for x in range(len(obj_1)))

    @classmethod
    def get_eq(cls, obj_1, obj_2):
        return all((obj_1[x] == obj_2[x] for x in range(len(obj_1))))

    @classmethod
    def verify_val(cls, obj_1, obj_2):
        if len(obj_1) != len(obj_2):
            raise ArithmeticError('Vector lengths don\'t match')

    def __add__(self, other):
        self.verify_val(self.coords, other.coords)
        return Vector(*(self.get_sum(self.coords, other.coords)))

    def __iadd__(self, other):
        if type(other) is int:
            self.coords = tuple(x + other for x in self.coords)
            return self
        if type(other) is Vector:
            self.coords = self.get_sum(self.coords, other.coords)
            return self

    def __sub__(self, other):
        self.verify_val(self.coords, other.coords)
        return Vector(*(self.get_dif(self.coords, other.coords)))

    def __isub__(self, other):
        if isinstance(other, int):
            self.coords = (x - other for x in self.coords)
            return self
        if isinstance(other, Vector):
            self.coords = self.get_dif(self.coords, other.coords)
            return self

    def __mul__(self, other):
        self.verify_val(self.coords, other.coords)
        return Vector(*(self.get_mult(self.coords, other.coords)))

    def __eq__(self, other):
        self.verify_val(self.coords, other.coords)
        return self.get_eq(self.coords, other.coords)


vec_1 = Vector(*(1, 2, 3, 4, 5))
print(vec_1.coords)
vec_2 = Vector(1, 2, 3, 4, 5)
vec_3 = vec_2 - vec_1
print(vec_3.coords)
print(vec_1 == vec_2)
