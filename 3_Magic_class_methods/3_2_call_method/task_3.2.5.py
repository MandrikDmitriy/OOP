class DigitRetrieve:
    def __call__(self, string, *args, **kwargs):
        if string.isdigit():
            return int(string)
        elif string[0] == '-' and string[1:].isdigit():
            return int(string)
        else:
            return None


dg = DigitRetrieve()
st = ['123', 'abc', '-56.3', '0', '-5', '-5ad']
digits = list(map(dg, st))
print(digits)
