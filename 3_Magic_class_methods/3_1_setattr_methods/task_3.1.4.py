class Shop:
    def __init__(self, name):
        self.name = name
        self.goods = []

    def add_product(self, product):
        self.goods.append(product)

    def remove_product(self, product):
        if product in self.goods:
            self.goods.remove(product)


class Product:
    _id_instance = 1
    attrs = {'name': (str,), 'weight': (int, float), 'price': (int, float), 'id': (int,)}

    def __init__(self, name, weight, price):
        self.name = name
        self.weight = weight
        self.price = price
        self.id = Product._id_instance
        Product._id_instance += 1

    def __setattr__(self, key, value):
        if key in self.attrs and type(value) in self.attrs[key]:
            if (key == 'price' or key == 'weight') and value <= 0:
                raise TypeError('Incorrect type of assigned data')
        elif key in self.attrs:
            raise TypeError('Incorrect type of assigned data')

        object.__setattr__(self, key, value)

    def __delattr__(self, item):
        if item == 'id':
            raise AttributeError('ID attribute cannot be deleted')
        else:
            object.__delattr__(self, item)


shop = Shop("Dmitriy and K")
book = Product('Python OOP', 100, 1024)
shop.add_product(book)
shop.add_product(Product('Python', 150, 512))
shop.add_product(Product('Un name', 300, 600))
for i in shop.goods:
    print(f'{i.id}, {i.name}, {i.weight}, {i.price}')
