class BookStudy:
    def __init__(self, name, author, year):
        self.name = name
        self.author = author
        self.year = year

    def __hash__(self):
        return hash((self.name.lower(), self.author.lower()))

    def __eq__(self, other):
        return hash(self) == hash(other)


with open('task_3.6.8.txt', 'r', encoding='utf-8') as file:
    lst_in = list(x.split(';') for x in file.read().splitlines())

lst_bs = list(BookStudy(*i) for i in lst_in)
unique_books = len(set(lst_bs))
print(unique_books)
