class FileAcceptor:
    def __init__(self, *args):
        self.file = args

    def __call__(self, val, *args, **kwargs):
        start = val.rfind('.')
        return val[start+1:] in self.file

    def __add__(self, other):
        if type(other) is not FileAcceptor:
            raise TypeError('The attribute must be a FileAcceptor class')
        s = tuple(x for x in other.file if x not in self.file)
        return FileAcceptor(self.file + s)


filenames = ["boat.jpg", "web.png", "text.txt", "python.doc", "ava.jpg", "forest.jpeg", "eq_1.png", "eq_2.png"]
acceptor = FileAcceptor('jpg', 'png', 'jpeg')
print(acceptor.file)
acceptor_2 = FileAcceptor('png', 'bmp')
acceptor_3 = acceptor + acceptor_2
print(acceptor_3.file)
filenames = list(filter(acceptor, filenames))
print(filenames)
