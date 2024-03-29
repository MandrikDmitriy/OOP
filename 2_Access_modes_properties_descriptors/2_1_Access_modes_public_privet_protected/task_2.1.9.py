class ObjList:
    def __init__(self, data=None):
        self.__next = None
        self.__prev = None
        self.__data = data

    def set_next(self, obj):
        self.__next = obj

    def set_prev(self, obj):
        self.__prev = obj

    def get_next(self):
        return self.__next

    def get_prev(self):
        return self.__prev

    def set_data(self, data):
        self.__data = data

    def get_data(self):
        return self.__data


class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def add_obj(self, obj):
        if self.tail is None and self.head is None:
            obj.set_next(self.tail)
            obj.set_prev(self.head)
            self.head = obj
            self.tail = obj
        else:
            self.tail.set_next(obj)
            obj.set_prev(self.tail)
            self.tail = obj

    def remove_obj(self):
        if self.tail is None:
            return
        ptr = self.tail.get_prev()
        if ptr:
            ptr.set_next(None)
        self.tail.set_prev(None)
        self.tail = ptr
        if self.tail is None:
            self.head = None

    def get_data(self):
        ptr = self.head
        s = []
        while ptr is not None:
            s.append(ptr.get_data())
            ptr = ptr.get_next()
        return s


ob = ObjList('data')
lst = LinkedList()
lst.add_obj(ObjList('data_1'))
lst.add_obj(ObjList('data_2'))
lst.add_obj(ObjList('data_3'))
lst.add_obj(ObjList('data_4'))
lst.add_obj(ObjList('data_5'))
lst.add_obj(ObjList('data_6'))
lst.remove_obj()
lst.remove_obj()
lst.remove_obj()
lst.remove_obj()
res = lst.get_data()
print(res)
