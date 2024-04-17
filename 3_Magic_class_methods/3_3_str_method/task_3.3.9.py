class Ingredient:
    def __init__(self, name, volume, measure):
        self.name = name
        self.volume = volume
        self.measure = measure

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name):
        if type(name) is str:
            self.__name = name

    @property
    def volume(self):
        return self.__volume

    @volume.setter
    def volume(self, value):
        if type(value) in (int, float):
            self.__volume = value

    @property
    def measure(self):
        return self.__measure

    @measure.setter
    def measure(self, value):
        if type(value) is str:
            self.__measure = value

    def __str__(self):
        return f'{self.name}: {self.volume}, {self.measure}'


class Recipe:
    def __init__(self, *args):
        self.recipe = list(args)

    def add_ingredient(self, ing):
        self.recipe.append(ing)

    def remove_ingredient(self, ing):
        self.recipe.remove(ing)

    def get_ingredient(self):
        return tuple(self.recipe)

    def __len__(self):
        return len(self.recipe)


recipe = Recipe()
recipe.add_ingredient(Ingredient('Salt', 1, 'one tablespoon'))
recipe.add_ingredient(Ingredient('Flour', 1, 'kg'))
recipe.add_ingredient(Ingredient('Mutton', 10, 'kg'))
ings = recipe.get_ingredient()
n = len(recipe)
print(ings, n)
