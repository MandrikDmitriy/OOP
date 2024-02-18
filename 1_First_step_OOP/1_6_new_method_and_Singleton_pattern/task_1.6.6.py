class AbstractClass:
    def __new__(cls, *args, **kwargs):
        return 'Ошибка: нельзя создать объекты абстрактного класса'


obj = AbstractClass()
print(obj)