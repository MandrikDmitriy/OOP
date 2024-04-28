class MoneyR:
    def __init__(self, volume=None):
        self.cd = None
        self.volume = volume

    @property
    def cd(self):
        return self.__cd

    @cd.setter
    def cd(self, val):
        self.__cd = val

    @property
    def volume(self):
        return self.__volume

    @volume.setter
    def volume(self, val):
        self.__volume = val

    @classmethod
    def verify_data(cls, data):
        if data.cd is None:
            raise ValueError("Exchange rates not determinate")

    @classmethod
    def get_rates(cls, obj):
        s = obj.cd.rates
        if type(obj) is MoneyR:
            return s.get('dollar')
        elif type(obj) is MoneyD:
            return s.get('rub')
        else:
            return s.get('euro') * s.get('rub')

    def __eq__(self, other):
        self.verify_data(self)
        self.verify_data(other)
        return self.volume == (other.volume * self.get_rates(other))

    def __lt__(self, other):
        self.verify_data(other)
        self.verify_data(self)
        return self.volume < (other.volume * self.get_rates(other))

    def __le__(self, other):
        self.get_rates(self)
        self.get_rates(other)
        return self.volume <= (other.volume * self.get_rates(other))


class MoneyD:
    def __init__(self, volume=None):
        self.cd = None
        self.volume = volume

    @property
    def cd(self):
        return self.__cd

    @cd.setter
    def cd(self, val):
        self.__cd = val

    @property
    def volume(self):
        return self.__volume

    @volume.setter
    def volume(self, val):
        self.__volume = val

    @classmethod
    def verify_data(cls, data):
        if data.cd is None:
            raise ValueError("Exchange rates not determinate")

    @classmethod
    def get_rates(cls, obj):
        s = obj.cd.rates
        if type(obj) is MoneyR:
            return s.get('dollar')
        elif type(obj) is MoneyD:
            return s.get('rub')
        else:
            return s.get('euro') * s.get('rub')

    def __eq__(self, other):
        self.verify_data(self)
        self.verify_data(other)
        return (self.volume * self.get_rates(self)) == (other.volume * self.get_rates(other))

    def __lt__(self, other):
        self.verify_data(other)
        self.verify_data(self)
        return (self.volume * self.get_rates(self)) < (other.volume * self.get_rates(other))

    def __le__(self, other):
        self.get_rates(self)
        self.get_rates(other)
        return (self.volume * self.get_rates(self)) <= (other.volume * self.get_rates(other))


class MoneyE:
    def __init__(self, volume=None):
        self.cd = None
        self.volume = volume

    @property
    def cd(self):
        return self.__cd

    @cd.setter
    def cd(self, val):
        self.__cd = val

    @property
    def volume(self):
        return self.__volume

    @volume.setter
    def volume(self, val):
        self.__volume = val

    @classmethod
    def verify_data(cls, data):
        if data.cd is None:
            raise ValueError("Exchange rates not determinate")

    @classmethod
    def get_rates(cls, obj):
        s = obj.cd.rates
        if type(obj) is MoneyR:
            return s.get('dollar')
        elif type(obj) is MoneyD:
            return s.get('rub')
        else:
            return s.get('euro') * s.get('rub')

    def __eq__(self, other):
        self.verify_data(self)
        self.verify_data(other)
        return (self.volume * self.get_rates(self)) == (other.volume * self.get_rates(other))

    def __lt__(self, other):
        self.verify_data(other)
        self.verify_data(self)
        return (self.volume * self.get_rates(self)) < (other.volume * self.get_rates(other))

    def __le__(self, other):
        self.get_rates(self)
        self.get_rates(other)
        return (self.volume * self.get_rates(self)) <= (other.volume * self.get_rates(other))


class CentralBank:
    rates = None

    def __new__(cls, *args, **kwargs):
        return None

    @classmethod
    def register(cls, money):
        money.cd = cls


CentralBank.rates = {'rub': 72.5, 'dollar': 1.0, 'euro': 1.15}
d = MoneyD(500)
r = MoneyR(450)
CentralBank.register(d)
CentralBank.register(r)

if r > d:
    print('no bad')
else:
    print('need more')
