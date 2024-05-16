class Dimensions:
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c

    @property
    def a(self):
        return self.__a

    @a.setter
    def a(self, val):
        if val > 0:
            self.__a = val
        else:
            raise ValueError('Overall dimension mast be positive numbers')

    @property
    def b(self):
        return self.__b

    @b.setter
    def b(self, val):
        if val > 0:
            self.__b = val
        else:
            raise ValueError('Overall dimension mast be positive numbers')

    @property
    def c(self):
        return self.__c

    @c.setter
    def c(self, val):
        if val > 0:
            self.__c = val
        else:
            raise ValueError('Overall dimension mast be positive numbers')

    def __hash__(self):
        return hash((self.a, self.b, self.c))


s_inp = '1 2 3; 4 5 6.78; 1 2 3; 3 1 2.5'
lst_dims = list(Dimensions(*map(float, x.split())) for x in s_inp.split('; '))
print(lst_dims)
lst_dims = sorted(lst_dims, key=hash)
print(lst_dims)
for i in lst_dims:
    print(i.a, i.b, i.c)
