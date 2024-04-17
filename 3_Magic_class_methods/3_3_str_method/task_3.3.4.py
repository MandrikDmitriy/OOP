class WordString:
    def __init__(self, string=None):
        self.__string = string

    @classmethod
    def new_list(cls, string):
        if string is None:
            return list()
        else:
            return [i for i in string.split()]

    @property
    def string(self):
        return self.__string

    @string.setter
    def string(self, value):
        self.__string = value

    def __len__(self):
        return len(self.new_list(self.string))

    def words(self, indx):
        if len(self.new_list(self.string)) + 1 < indx:
            return
        return self.new_list(self.string)[indx]


word = WordString()
word.string = "Course of Python"
n = len(word)
first = '' if n == 0 else word.words(0)
print(word.string)
print(f'Count words: {n}; first word: {first}')
