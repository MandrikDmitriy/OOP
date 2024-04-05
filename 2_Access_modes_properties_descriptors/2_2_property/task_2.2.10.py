class PhoneBook:
    def __init__(self):
        self.phone_list = []

    def add_phone(self, phone):
        self.phone_list.append(phone)

    def remove_phone(self, indx):
        self.phone_list.pop(indx)

    def get_phone_list(self):
        return self.phone_list


class PhoneNumber:
    def __init__(self, number, fio):
        if self.check_number(number) and self.check_fio(fio):
            self.number = number
            self.fio = fio

    @classmethod
    def check_number(cls, number):
        return type(number) is int and len(str(number)) == 11

    @classmethod
    def check_fio(cls, fio):
        return type(fio) is str


p = PhoneBook()
p.add_phone(PhoneNumber(12345678901, "DM"))
p.add_phone(PhoneNumber(23456789012, 'MD'))
phones = p.get_phone_list()
p.remove_phone(1)
print(phones)
print(p.phone_list[0].number)