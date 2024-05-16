class React:
    def __init__(self, x, y, width, height):
        self.x = x
        self.y = y
        self.width = width
        self.height = height

    def __hash__(self):
        return hash((self.height, self.width))


r1 = React(10, 5, 100, 50)
r2 = React(-10, 4, 100, 50)

h1, h2 = hash(r1), hash(r2)
print(h1 == h2)
print(h1, h2, sep='\n')
