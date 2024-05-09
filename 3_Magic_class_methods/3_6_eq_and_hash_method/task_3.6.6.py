class ShopItem:
    def __init__(self, name, weight, price):
        self.name = name
        self.weight = weight
        self.price = price

    def __hash__(self):
        return hash((self.name.lower(), self.weight, self.price))

    def __eq__(self, other):
        return hash(self) == hash(other)


with open('task_3.6.6.txt', 'r', encoding='utf-8') as file:
    line = list(x.split(": ") for x in file.read().splitlines())
print(line)
shop_item = {}
i = 0
for k in line:
    w, p = k[1].split()
    sh = ShopItem(k[0], w, p)
    val = [sh, 0]
    if sh in shop_item:
        f = shop_item[sh]
        f[1] += 1
        shop_item[sh] = f
    else:
        shop_item[sh] = val

print(shop_item)
