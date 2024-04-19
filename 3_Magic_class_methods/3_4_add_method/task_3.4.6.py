class StackObj:
    def __init__(self, data):
        self.__data = data
        self.__next = None

    @property
    def data(self):
        return self.__data

    @property
    def next(self):
        return self.__next

    @next.setter
    def next(self, val):
        self.__next = val


class Stack:
    def __init__(self):
        self.top = None
        self.tail = None

    def push_back(self, obj):
        self.__varify_val(obj)
        if self.top is None:
            self.top = self.tail = obj
        else:
            self.tail.next = obj
            self.tail = obj

    def pop_back(self):
        if self.top == self.tail:
            self.top = self.tail = None
        else:
            node = self.top
            while node.next != self.tail:
                node = node.next
            self.tail = node
            self.tail.next = None

    def get_list(self):
        h = self.top
        s = []
        while h.next is not None:
            s.append(h.data)
            h = h.next
        s.append(h.data)
        return s

    @staticmethod
    def __varify_val(value):
        if not isinstance(value, StackObj):
            raise TypeError("Incorrect class data type!")

    def __add__(self, other):
        self.__varify_val(other)
        self.push_back(other)
        return self

    def __mul__(self, other):
        for val in other:
            self.__add__(StackObj(val))
        return self

    def __iadd__(self, other):
        return self.__add__(other)

    def __imul__(self, other):
        return self.__mul__(other)


st = Stack()
st.push_back(StackObj('data_1'))
st.push_back(StackObj('data_2'))
st = st + StackObj('data_3')
st += StackObj('data_4')
st = st * ['data_5', 'data_6', 'data_7']
st *= ['data_8', 'data_9', 'data_10']
st.pop_back()
st.pop_back()
print(st.get_list())
