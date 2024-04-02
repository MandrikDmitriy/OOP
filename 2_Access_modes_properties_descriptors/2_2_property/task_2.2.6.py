class StackObj:
    def __init__(self, data):
        self.__data = data
        self.__next = None

    @property
    def data(self):
        return self.__data

    @data.setter
    def data(self, data):
        self.__data = data

    @property
    def next(self):
        return self.__next

    @next.setter
    def next(self, obj):
        if isinstance(obj, StackObj) or obj is None:
            self.__next = obj


class Stack:
    def __init__(self):
        self.top = None
        self.last_obj = None

    def push(self, obj):
        if self.top is None:
            self.top = obj
            self.last_obj = self.top
        else:
            self.last_obj.next = obj
            self.last_obj = obj

    def pop(self):
        h = self.top
        if h is None:
            return
        while h and h.next != self.last_obj:
            h = h.next
        if h:
            h.next = None
        last = self.last_obj
        self.last_obj = h
        if self.last_obj is None:
            self.top = None
        return last

    def get_data(self):
        s = []
        ptr = self.top
        while ptr is not None:
            s.append(ptr.data)
            ptr = ptr.next
        return s


obj_1 = StackObj('data')
st = Stack()
st.push(StackObj('data_1'))
st.push(StackObj('data_2'))
print(st.pop())
st.push(StackObj('data_3'))
print(st.get_data())

