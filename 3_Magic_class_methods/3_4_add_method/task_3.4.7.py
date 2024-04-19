class Book:
    def __init__(self, title, author, year):
        self.title = title
        self.author = author
        self.year = year

    @property
    def title(self):
        return self.__title

    @title.setter
    def title(self, val):
        if type(val) is str:
            self.__title = val

    @property
    def author(self):
        return self.__author

    @author.setter
    def author(self, val):
        if type(val) is str:
            self.__author = val

    @property
    def year(self):
        return self.__year

    @year.setter
    def year(self, val):
        if type(val) is int:
            self.__year = val


class Lib:
    def __init__(self):
        self.book_list = []

    def __len__(self):
        return len(self.book_list)

    def __add__(self, other):
        self.book_list.append(other)
        return self

    def __iadd__(self, other):
        return self.__add__(other)

    def __sub__(self, other):
        if isinstance(other, Book):
            self.book_list.remove(other)
        else:
            self.book_list.pop(other)
        return self

    def __isub__(self, other):
        return self.__sub__(other)


lib = Lib()
book_1 = Book('book_1', 'A', 2001)
book_2 = Book("book_2", 'S', 2002)
book_3 = Book('book_3', 'D', 2003)
lib = lib + book_1
lib = lib + book_2
lib += book_3
print(len(lib))
lib = lib - book_2
lib -= book_3
print(len(lib))
