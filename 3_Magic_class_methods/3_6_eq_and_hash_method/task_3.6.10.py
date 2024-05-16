class TrValue:
    @classmethod
    def validate_val(cls, val):
        if type(val) not in (int, float) or val <= 0:
            raise ValueError('Overall dimensions must be positive numbers')

    def __set_name__(self, owner, name):
        self.name = '__' + name

    def __get__(self, instance, owner):
        return getattr(instance, self.name, None)

    def __set__(self, instance, value):
        self.validate_val(value)
        setattr(instance, self.name, value)


class Triangle:
    a = TrValue()
    b = TrValue()
    c = TrValue()

    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c
        self.validate_triangle(self.a, self.b, self.c)

    @classmethod
    def validate_triangle(cls, a, b, c):
        if b + c < a or a + c < b or a + b < c:
            raise ValueError('With the specified lengths it is impossible to create a triangle')

    def __len__(self):
        return int(sum((self.a, self.b, self.c)))

    def __call__(self, *args, **kwargs):
        a, b, c = self.a, self.b, self.c
        p = 0.5 * (a + b + c)
        s = (p * (p - a) * (p - b) * (p - c)) ** 0.5
        return s


tr = Triangle(2, 2, 3)
print(len(tr))
print(tr())
