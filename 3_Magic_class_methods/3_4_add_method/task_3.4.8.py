class Item:
    def __init__(self, name, money):
        self.name = name
        self.money = money

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name):
        self.__name = name if type(name) is str else ''

    @property
    def money(self):
        return self.__money

    @money.setter
    def money(self, val):
        self.__money = val if type(val) in (int, float) else 0

    def __add__(self, other):
        return self.money + other.money


class Budget:
    def __init__(self):
        self.my_budget = []

    def add_item(self, it):
        self.my_budget.append(it)

    def remove_item(self, ind):
        self.my_budget.pop(ind)

    def get_items(self):
        return self.my_budget


my_budget = Budget()
my_budget.add_item(Item('Python course', 2000))
my_budget.add_item(Item('Django course', 5000.01))
my_budget.add_item(Item('NumPy course', 0))
my_budget.add_item(Item('C++ course', 1500.10))
s = 0
for i in my_budget.get_items():
    s = s + i.money
print(s)
res = Item('Python course', 2000) + Item('Django course', 5000.01)
print(res)
