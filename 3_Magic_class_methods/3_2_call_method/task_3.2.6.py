class RenderList:
    correct_type_list = ['ul', 'ol']

    def __init__(self, type_list):
        self.type_list = type_list

    def __setattr__(self, key, value):
        if value not in self.correct_type_list:
            value = 'ul'
            object.__setattr__(self, key, value)
        else:
            object.__setattr__(self, key, value)

    def __call__(self, lst, *args, **kwargs):
        # menu = [f'<li>{i}</li>' for i in lst]
        # firs_tag = [f'<{self.type_list}>']
        # last_tag = [f'</{self.type_list}>']
        # html = firs_tag + menu + last_tag
        # return '\n'.join(html)
        return '\n'.join([f'<{self.type_list}>', *map(lambda x: f'<li>{x}</li>', lst), f'</{self.type_list}>'])


lst_1 = ['menu_1', 'menu_2', 'menu_3', 'menu_4']
render = RenderList('kl')
html = render(lst_1)
print(html)
