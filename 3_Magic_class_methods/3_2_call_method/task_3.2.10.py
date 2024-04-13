class InputValue:
    def __init__(self, render):
        self.render = render

    def __call__(self, func):
        def wrapper(*args, **kwargs):
            return list(map(self.render, func(*args, **kwargs).split()))
        return wrapper


class RenderDigit:
    def __call__(self, value,  *args, **kwargs):
        if value.isdigit():
            return int(value)
        elif value[0] == '-' and value[1:].isdigit():
            return int(value)
        else:
            return None


render = RenderDigit()
input_dg = InputValue(render)(input)
res = input_dg()
print(res)
