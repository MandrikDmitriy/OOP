import sys


class StreamDate:
    def create(self, fields, lst_values):
        if len(fields) != len(lst_values):
            return False
        for i, key in enumerate(fields):
            setattr(self, key, lst_values[i])

        return True


class StreamReader:
    FIELDS = ('id', 'title', 'pages')

    def readLines(self):
        lst_in = list(map(str.strip, sys.stdin.readline()))
        sd = StreamDate()
        res = sd.create(self.FIELDS, lst_in)
        return sd, res


sr = StreamReader()
data, result = sr.readLines()

print(data, result)