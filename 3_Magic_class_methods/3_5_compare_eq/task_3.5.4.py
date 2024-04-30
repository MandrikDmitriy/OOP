class Dimensions:
    MIN_DIMENSIONS = 10
    MAX_DIMENSIONS = 10000

    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c

    def __call__(self, *args, **kwargs):
        return self.__get_dim()

    @classmethod
    def __valid_data(cls, val):
        return cls.MIN_DIMENSIONS <= val <= cls.MAX_DIMENSIONS

    @property
    def a(self):
        return self.__a

    @a.setter
    def a(self, val):
        if self.__valid_data(val):
            self.__a = val

    @property
    def b(self):
        return self.__b

    @b.setter
    def b(self, val):
        if self.__valid_data(val):
            self.__b = val

    @property
    def c(self):
        return self.__c

    @c.setter
    def c(self, val):
        if self.__valid_data(val):
            self.__c = val

    def __get_dim(self):
        return self.a * self.b * self.c

    def __lt__(self, other):
        return self.__get_dim() > other.__get_dim()

    def __ge__(self, other):
        return self.__get_dim() >= other.__get_dim()


class ShopItem:
    def __init__(self, name, price, dim):
        self.name = name
        self.price = price
        self.dim = dim


def sort_key(k):
    return k.dim()


lst_shop = list()
lst_shop.append(ShopItem('sneakers', 1024, Dimensions(40, 30, 120)))
lst_shop.append(ShopItem('umbrella', 500, Dimensions(10, 20, 50)))
lst_shop.append(ShopItem('fridge', 40000, Dimensions(2000, 600, 500)))
lst_shop.append(ShopItem('stool', 2000, Dimensions(500, 200, 200)))
lst_shop_sorted = list(sorted(lst_shop, key=sort_key))
print(list(map(lambda x: f'{x.name} : {x.price} : {x.dim()}', lst_shop)))
print(list(map(lambda x: f'{x.name} : {x.price} : {x.dim()}', lst_shop_sorted)))
