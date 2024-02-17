class Cart:
    def __init__(self):
        self.goods = []

    def add(self, gd):
        self.goods.append(gd)

    def remove(self, ind):
        self.goods.pop(ind)

    def get_list(self):
        return [f'{x.name}:{x.price}' for x in self.goods]


class Table:
    def __init__(self, name, price):
        self.name = name
        self.price = price


class TV:
    def __init__(self, name, price):
        self.name = name
        self.price = price


class Notebook:
    def __init__(self, name, price):
        self.name = name
        self.price = price


class Cup:
    def __init__(self, name, price):
        self.name = name
        self.price = price


cart = Cart()
cart.add(TV('Samsung', 100))
cart.add(TV('Sony', 200))
cart.add(Table('table', 50))
cart.add(Notebook('Asus', 500))
cart.add(Notebook('Dell', 800))
cart.add(Cup('just_cup', 5))
print(cart.get_list())