from string import ascii_lowercase, digits


class CardCheck:
    CHARS_FOR_NAME = ascii_lowercase.upper() + digits

    @staticmethod
    def check_card_number(number):
        if type(number) != str or number.count('-') != 3 or len(number) != 19:
            return False
        for i in number.split('-'):
            if len(i) != 4 or not set(i) < set(digits):
                return False
        return True

    @classmethod
    def check_name(cls, name):
        if type(name) != str or name.count(' ') != 1:
            return False
        for i in name.split():
            if not set(i) <= set(cls.CHARS_FOR_NAME):
                return False
        return True


is_number = CardCheck.check_card_number("1234-4567-9012-0000")
is_name = CardCheck.check_name("DMITRI MANDRIK")
print(is_number)
print(is_name)
