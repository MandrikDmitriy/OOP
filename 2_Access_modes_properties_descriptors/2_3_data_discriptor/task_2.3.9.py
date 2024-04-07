class Bag:
    def __init__(self, max_weight):
        self.max_weight = max_weight
        self.__things = []

    @property
    def things(self):
        return self.__things

    def add_thing(self, thing):
        if self.max_weight - self.get_total_weight() >= thing.weight:
            self.__things.append(thing)

    def remove_thing(self, indx):
        self.__things.pop(indx)

    def get_total_weight(self):
        return sum(map(lambda x: x.weight, self.things))


class Thing:
    def __init__(self, name, weight):
        self.name = name
        self.weight = weight


bag = Bag(1000)
bag.add_thing(Thing('Python book', 100))
bag.add_thing(Thing('Phone', 500))
bag.add_thing(Thing('Bottle of water', 200))
bag.add_thing(Thing('Pan', 50))
w = bag.get_total_weight()
for t in bag.things:
    print(f'{t.name}: {t.weight}')
print(bag.things)
print(bag.get_total_weight())
