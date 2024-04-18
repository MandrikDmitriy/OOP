class ListMath:
    def __init__(self, lst_in=None):
        self.lst_math = lst_in if type(lst_in) is list else []
        self.lst_math = list(filter(lambda x: type(x) in (int, float), self.lst_math))

    @staticmethod
    def __check_value(value):
        if type(value) not in (int, float):
            raise TypeError('Incorrect data type')

    def __add__(self, other):
        self.__check_value(other)
        return ListMath([i + other for i in self.lst_math])

    def __radd__(self, other):
        self.__check_value(other)
        return ListMath([other + i for i in self.lst_math])

    def __sub__(self, other):
        self.__check_value(other)
        return ListMath([i - other for i in self.lst_math])

    def __rsub__(self, other):
        self.__check_value(other)
        return ListMath([other - i for i in self.lst_math])

    def __mul__(self, other):
        self.__check_value(other)
        return ListMath([i * other for i in self.lst_math])

    def __rmul__(self, other):
        self.__check_value(other)
        return ListMath([other * i for i in self.lst_math])

    def __truediv__(self, other):
        self.__check_value(other)
        return ListMath([i / other for i in self.lst_math])

    def __rtruediv__(self, other):
        self.__check_value(other)
        return ListMath([other / i for i in self.lst_math])

    def __iadd__(self, other):
        self.__check_value(other)
        self.lst_math = [i + other for i in self.lst_math]
        return self

    def __isub__(self, other):
        self.__check_value(other)
        self.lst_math = [i - other for i in self.lst_math]
        return self

    def __imul__(self, other):
        self.__check_value(other)
        self.lst_math = [i * other for i in self.lst_math]
        return self

    def __itruediv__(self, other):
        self.__check_value(other)
        self.lst_math = [i / other for i in self.lst_math]
        return self


lst = ListMath([1, 'abs', -5, 7.68, True])
lst = lst + 76
lst = 6.5 + lst
lst += 76.7
lst = lst - 76
lst = 7.0 - lst
lst -= 76.3
lst = lst * 5
lst = 5 * lst
lst *= 5
lst = lst / 13
lst = 3 / lst
lst /= 13.0
