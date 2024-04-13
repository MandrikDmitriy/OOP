class HandlerGET:
    def __init__(self, func):
        self.func = func

    def get(self, func, request, *args, **kwargs):
        return f'{request.get('method')}: {func(request)}'

    def __call__(self, request, *args, **kwargs):
        m = request.get('method', 'GET ')
        if m == 'GET':
            return self.get(self.func, request)
        return None


@HandlerGET
def contact(request):
    return "Dmitriy Mandrik"


res = contact({'method': 'GET', 'url': 'contact.html'})
print(res)
