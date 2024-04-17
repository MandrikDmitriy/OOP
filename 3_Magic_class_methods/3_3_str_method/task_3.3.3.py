class Model:
    def __init__(self):
        self.data = {}
        self.value = []

    def query(self, **kwargs):
        self.data = kwargs

    def __str__(self):
        if len(self.data) == 0:
            return 'Model'
        else:
            return 'Model: ' + ', '.join(list(f'{key} = {value}' for key, value in self.data.items()))
            # return 'Model: ' + ', '.join(list(map(lambda x: f'{x} = {self.data[x]}', self.data)))


model = Model()
model.query(id=1, fio='Sergey', old=33)
print(model)
