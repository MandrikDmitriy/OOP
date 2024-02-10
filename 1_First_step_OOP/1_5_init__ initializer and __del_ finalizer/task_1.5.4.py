import random


class Line:
    def __init__(self, a, b, c, d):
        self.sp = (a, b)
        self.ep = (c, d)


class Rect:
    def __init__(self, a, b, c, d):
        self.sp = (a, b)
        self.ep = (c, d)


class Ellipse:
    def __init__(self, a, b, c, d):
        self.sp = (a, b)
        self.ep = (c, d)


random.seed(1)

elements = []
for i in range(217):
    a = random.randint(0,9)
    b = random.randint(0, 9)
    c = random.randint(0, 9)
    d = random.randint(0, 9)
    figure = random.choice([Line, Rect, Ellipse])
    if figure == Line:
        a = b = c = d = 0
    elements.append(figure(a, b, c, d))

# elements = [(Line, Rect, Ellipse)[random.randint(0, 2)](1, 2, 3, 4) for i in range(217)]
# for obj in elements:
#     if isinstance(obj, Line):
#         obj.ep = obj.sp = 0, 0