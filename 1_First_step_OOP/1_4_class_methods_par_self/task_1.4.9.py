import sys

lst_in = ['1 2 3 4', '5 6 7 8', '9 10 11 12']

class DateBase:
    lst_data = []
    FIELDS = ('id', 'name', 'old', 'salary')
    def insert(self,data):
        # self.lst_data = list({self.FIELDS[ind]: key for ind, key in enumerate(i.split())} for i in data)
        for i in data:
            self.lst_data.append(dict(zip(self.FIELDS, i.split())))

    def select(self, a, b):
        if b - a > len(self.lst_data):
            return self.lst_data[a:len(self.lst_data)]
        else:
            return self.lst_data[a:b+1]


db = DateBase()
db.insert(lst_in)
print(db.lst_data)