class Morph:
    def __init__(self, *args):
        self.lst_words = [i.strip(' ,!?.;').lower() for i in args[0]]

    def add_word(self, word):
        if word.lower() not in self.lst_words:
            self.lst_words.append(word)

    def get_word(self):
        return tuple(self.lst_words)

    def __eq__(self, other):
        if type(other) is not str:
            raise ValueError('The operand must be a string')
        return other.lower() in self.lst_words


with open('task_3.5.6.txt', 'r', encoding='utf-8') as file:
    line = [lst.split(', ') for lst in file.read().splitlines()]
print(line)
dict_words = [Morph(i) for i in line]
for i in dict_words:
    print(i)
text_input = "Мы будем устанавливать связь завтра днем."
words = map(lambda x: x.strip(',!?.;').lower(), text_input.split())
res = sum(word == morph for word in words for morph in dict_words)
print(res)
