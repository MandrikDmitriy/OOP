class WindowDlg:
    def __init__(self, title, width, height):
        self.__title = title
        self.__width = width
        self.__height = height

    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, value):
        if type(value) is int and 0 <= value <= 10000:
            self.__width = value
            self.show()

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, value):
        if type(value) is int and 0 <= value <= 10000:
            self.__height = value
            self.show()

    def show(self):
        print(f'{self.__title}: {self.__width}, {self.__height}')


win = WindowDlg('picture', 100, 200)
win.show()
win.height = 300
