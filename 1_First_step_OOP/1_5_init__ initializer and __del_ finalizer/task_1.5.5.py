class TriangleChecker:
    def __init__(self, a=1, b=2, c=4):
        self.a = a
        self.b = b
        self.c = c

    def is_triangle(self):
        # if not all(map(lambda x: type(x) in (int, float), (self.a, self.b, self.c))):
        if not isinstance(self.a and self.b and self.c, (int, float)):
            return 1
        elif not all(map(lambda x: x > 0, (self.a, self.b, self.c))):
            return 1
        elif self.a + self.b <= self.c or self.b + self.c <= self.a or self.a + self.c <= self.b:
            return 2
        else:
            return 3


tp = TriangleChecker(3,4,5)
print(tp.is_triangle())
