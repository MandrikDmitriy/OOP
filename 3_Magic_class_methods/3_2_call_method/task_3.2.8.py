class Handler:
    def __init__(self, methods=('GET',)):
        self.methods = methods

    def __call__(self, func, *args, **kwargs):
        def wrapper(request):
            m = request.get('method', "GET")
            if m in self.methods:
                method = m.lower()
                return self.__getattribute__(method)(func, request)
        return wrapper

    def get(self, func, request, *args, **kwargs):
        return f'{request.get('method')}:{func(request)}'

    def post(self, func, request, *args, **kwargs):
        return f'{request.get('method')}:{func(request)}'


@Handler(methods=('POST', 'GET'))
def contact(request):
    return "Dmitriy Mandrik"


res = contact({'method': 'POST', 'url': 'contact.html'})
print(res)
