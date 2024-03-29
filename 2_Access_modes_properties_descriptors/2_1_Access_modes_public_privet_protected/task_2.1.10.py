from random import randint
from string import ascii_letters, digits


class EmailValidator:

    EMAIL_CHARS = ascii_letters + digits + '_.'

    def __new__(cls, *args, **kwargs):
        return None

    @classmethod
    def get_random_emails(cls):
        n = randint(1, 100)
        length = len(cls.EMAIL_CHARS) - 1
        return ''.join(cls.EMAIL_CHARS[randint(0, length)] for i in range(n)) + '@gmail.ru'

    @classmethod
    def check_email(cls, email):
        if not cls.__is_email_str(email):
            return False
        ind = email.index('@')
        if not set(email) <= set(cls.EMAIL_CHARS + '@') or email.count('@') != 1:
            return False
        elif ind > 100 or len(email) - ind > 50:
            return False
        elif '.' not in email[ind:] or '..' in email[ind:]:
            return False
        else:
            return True

    @staticmethod
    def __is_email_str(email):
        return type(email) is str


print(EmailValidator.check_email('sc_lib@list.ru'))
print(EmailValidator.check_email('sc_lib@list_ru'))
print(EmailValidator.check_email('sc_lib@list..ru'))
print(EmailValidator.check_email('sc_lib!@list.ru'))
