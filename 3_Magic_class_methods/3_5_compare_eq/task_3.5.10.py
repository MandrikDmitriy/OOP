class Box:
    def __init__(self):
        self.box = []

    def add_thing(self, obj):
        if type(obj) is Thing:
            self.box.append(obj)

    def get_things(self):
        return self.box

    def __eq__(self, other):
        if len(self.box) != len(other.box):
            return False

        s = all([any([(i.name.lower() == k.name.lower() and i.mass == k.mass) for i in self.box]) for k in other.box])
        return s


class Thing:
    def __init__(self, name, mass):
        self.name = name
        self.mass = mass

    def __eq__(self, other):
        return self.name.lower() == other.name.lower() and self.mass == other.mass


b1 = Box()
b2 = Box()

b1.add_thing(Thing('chalk', 100))
b1.add_thing(Thing('rag', 200))
b1.add_thing(Thing('board', 2000))

b2.add_thing(Thing('Rag', 200))
b2.add_thing(Thing('Chalk', 100))
b2.add_thing(Thing('Board', 2000))

print(b1 == b2)
print(b1 != b2)
