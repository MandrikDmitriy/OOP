class StringText:
    def __init__(self, lst_word):
        self.lst_word = list(lst_word)

    def __len__(self):
        return len(self.lst_word)

    def __gt__(self, other):
        return len(self) > len(other)

    def __ge__(self, other):
        return len(self) >= len(other)


stich = ["Я к вам пишу — чего же боле?",
         "Что я могу еще сказать?",
         "Теперь, я знаю, в вашей воле",
         "Меня презреньем наказать.",
         "Но вы, к моей несчастной доле",
         "Хоть каплю жалости храня,",
         "Вы не оставите меня."]

strip_chars = '—?!,.;'
lst_text = [StringText(x.strip(strip_chars) for x in line.split() if len(x.strip(strip_chars)) > 0) for line in stich]
lst_text_sorted = sorted(lst_text, reverse=True)
lst_text_sorted = [' '.join(x.lst_word) for x in lst_text_sorted]
print(lst_text_sorted)
