class Body:
    def __init__(self, name, ro, volume):
        self.name = name if type(name) is str else None
        self.ro = ro if type(ro) in (int, float) else None
        self.volume = volume if type(volume) in (int, float) else None

    def get_weight(self):
        return self.ro * self.volume

    def __eq__(self, other):
        s = other.get_weight() if type(other) is Body else other
        return self.get_weight() == s

    def __lt__(self, other):
        s = other.get_weight() if type(other) is Body else other
        return self.get_weight() < s


body_1 = Body('Sasha', 1.3, 10)
body_2 = Body('Pety', 1.3,  10)

print(body_1 > body_2)
print(body_1 == body_2)
print(body_1 == 13)
print(body_1 < 8)
