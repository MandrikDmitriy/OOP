class Translator:

    def add(self, eng, rus):
        if 'new_dict' not in self.__dict__:
            self.new_dict = {}
        if eng in self.new_dict and rus not in self.new_dict[eng]:
            self.new_dict[eng] += [rus]
        else:
            self.new_dict.setdefault(eng, [rus])

    def remove(self, eng):
        del self.new_dict[eng]

    def translate(self, eng):
        return self.new_dict.get(eng)


new_lst = [('tree', 'дерево'), ('car', 'машина'), ('car', 'автомобиль'),
           ('leaf', 'лист'), ('river', 'река'), ('go', 'идти'), ('go', 'ехать'),
           ('go', 'ходить'), ('milk', 'молоко'), ('go', 'идти')]
tp = Translator()
for key, val in new_lst:
    tp.add(key, val)
tp.remove('car')
print(*tp.translate('go'))
print(*zip(tp.new_dict))



