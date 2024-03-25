class Point:
    def __init__(self, x, y):
        self.__x = self.__y = 0
        if self.__check_point(x, y):
            self.__x = x
            self.__y = y

    def get_coords(self):
        return self.__x, self.__y

    @classmethod
    def __check_point(cls, x, y):
        return type(x) in (int, float) and type(y) in (int, float)

class Rectangle:
    def __init__(self, sp, ep, *args):
        pass



rect = Rectangle(1, 2, 3,4)