class ListObject:
    def __init__(self, data):
        self.data = data
        self.next_obj = None

    def link(self, obj):
        self.next_obj = obj


lst_in = ['one', 'two', 'three', 'four', 'five']
head_obj = ListObject(lst_in[0])
obj = head_obj
for i in range(1, len(lst_in)):
    next_obj = ListObject(lst_in[i])
    obj.link(next_obj)
    obj = next_obj

