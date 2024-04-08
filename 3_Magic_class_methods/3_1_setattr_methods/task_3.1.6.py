class Museum:
    def __init__(self, name):
        self.name = name
        self.exhibits = []

    def add_exhibit(self, obj):
        self.exhibits.append(obj)

    def remove_exhibits(self, obj):
        if obj in self.exhibits:
            self.exhibits.remove(obj)

    def get_info_exhibit(self, indx):
        if len(self.exhibits) - 1 >= indx:
            return f'Description of the exhibit {self.exhibits[indx].name}: {self.exhibits[indx].descr}'


class Picture:
    def __init__(self, name, author, descr):
        self.name = name
        self.author = author
        self.descr = descr


class Mummies:
    def __init__(self, name, location, descr):
        self.name = name
        self.location = location
        self.descr = descr


class Papyri:
    def __init__(self, name, date, descr):
        self.name = name
        self.date = date
        self.descr = descr


mus = Museum("Hermitage")
mus.add_exhibit(Picture('Latter to the Sultan', 'Not author', 'This is picture the best!'))
mus.add_exhibit(Mummies('Dmitriy', 'Belarus', 'This is just man'))
mus.add_exhibit(Papyri('Lecture', 'Europa', 'This is just book'))
for x in mus.exhibits:
    print(x.descr)
print(mus.get_info_exhibit(1))
