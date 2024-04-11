class Book:
    attrs = {'title': str, 'author': str, 'pages': int, 'year': int}

    def __init__(self, title='', author='', pages=0, year=0):
        self.title = title
        self.author = author
        self.pages = pages
        self.year = year

    def __setattr__(self, key, value):
        if key in self.attrs and self.attrs[key] is type(value):
            super().__setattr__(key, value)
        else:
            raise TypeError('Incorrect type of assigned data')
        # if key == 'author' or key == 'title':
        #     if type(value) is not str:
        #         raise TypeError('Incorrect type of assigned data')
        # elif key == 'pages' or key == 'year':
        #     if type(value) is not int:
        #         raise TypeError('Incorrect type of assigned data')
        # else:
        #     object.__setattr__(key, value)


book = Book()
book.author = 'Dmitriy Mandrik'
book.title = 'Python OOP'
book.pages = 123
book.year = 2024
print(book.author)
