class Circle:
    attr = {'x': (int, float), 'y': (int, float), 'radius': (int, float)}

    def __init__(self, x, y, radius):
        self.__x = self.__y = self.__radius = None
        self.x = x
        self.y = y
        self.radius = radius

    @property
    def x(self):
        return self.__x

    @x.setter
    def x(self, val):
        self.__x = val

    @property
    def y(self):
        return self.__y

    @y.setter
    def y(self, val):
        self.__y = val

    @property
    def radius(self):
        return self.__radius

    @radius.setter
    def radius(self, val):
        self.__radius = val

    def __setattr__(self, key, value):
        if key in self.attr and type(value) not in self.attr[key]:
            raise TypeError("Incorrect data type")
        if key == 'radius' and value <= 0:
            return
        object.__setattr__(self, key, value)

    def __getattr__(self, item):
        return False


circle = Circle(10.5, 7, 22)
circle.radius = -10
x, y = circle.x, circle.y
res = circle.name
print(circle.x, circle.y, res)
