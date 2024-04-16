class RadiusVector:
    def __init__(self, *args):
        if len(args) == 1:
            self.__coords = [0] * args[0]
        else:
            self.__coords = list(args)

    def set_cords(self, *args):
        if len(args) > len(self.__coords):
            for i in range(len(self.__coords)):
                self.__coords[i] = args[i]
        else:
            for i in range(len(args)):
                self.__coords[i] = args[i]

    def get_cords(self):
        return tuple(self.__coords)

    def __len__(self):
        return len(self.__coords)

    def __abs__(self):
        return (sum(map(lambda x: x * x, self.__coords))) ** 0.5


vector3D = RadiusVector(3)
vector3D.set_cords(3, -5.6, 8)
a, b, c = vector3D.get_cords()
vector3D.set_cords(3, -5.6, 8, 10, 11)
vector3D.set_cords(1, 2)
res_len = len(vector3D)
res_abs = abs(vector3D)
print(res_len, res_abs, vector3D.get_cords())
