class ImageFileAcceptor:
    def __init__(self, extensions):
        self.extensions = extensions

    def __call__(self, file, *args, **kwargs):
        # left_val, right_val = file.split('.')
        # return right_val in self.extensions
        start = file.rfind('.')
        ext = "" if start == -1 else file[start + 1:]
        return ext in self.extensions


filenames = ["boat.jpg", "web.png", "text.txt", "python.doc", "ava.jpg", "forest.jpeg", "eq_1.png", "eq_2.png"]
acceptor = ImageFileAcceptor(('jpg', 'bmp', 'jpeg'))
image_filenames = filter(acceptor, filenames)
print(list(image_filenames))
