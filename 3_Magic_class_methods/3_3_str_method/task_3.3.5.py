class ObjList:
    def __init__(self, data):
        self.__data = ''
        self.data = data
        self.__prev = self.__next = None

    @property
    def data(self):
        return self.__data

    @data.setter
    def data(self, value):
        if type(value) is str:
            self.__data = value

    @property
    def prev(self):
        return self.__prev

    @prev.setter
    def prev(self, obj):
        if type(obj) in (ObjList, type(None)):
            self.__prev = obj

    @property
    def next(self):
        return self.__next

    @next.setter
    def next(self, obj):
        if type(obj) in (ObjList, type(None)):
            self.__next = obj


class LinkedList:
    count_index = 0

    def __init__(self):
        self.head = self.tail = None

    def add_obj(self, obj):
        if self.head is None:
            self.head = obj
            self.tail = obj
            self.count_index += 1
        else:
            obj.prev = self.tail
            self.tail.next = obj
            self.tail = obj
            self.count_index += 1

    def remove_obj(self, indx):
        if self.count_index - 1 < indx:
            raise IndexError("Incorrect index")
        if indx == 0:
            self.head = self.head.next
            self.head.prev = None
            self.count_index -= 1
        elif self.count_index - 1 == indx:
            self.tail = self.tail.prev
            self.tail.next = None
            self.count_index -= 1
        else:
            last_obj = self.head
            for i in range(indx + 1):
                last_obj = last_obj.next
            left_obj = last_obj.prev
            right_obj = last_obj.next
            left_obj.next = right_obj
            right_obj.prev = left_obj
            self.count_index -= 1

    def __len__(self):
        return self.count_index

    def linked_lst(self, indx):
        if self.count_index - 1 < indx:
            raise IndexError("Incorrect index")
        if indx == 0:
            return self.head.data
        elif self.count_index - 1 == indx:
            return self.tail.data
        else:
            last_obj = self.head
            for i in range(indx):
                last_obj = last_obj.next
            return last_obj.data

    def __call__(self, indx, *args, **kwargs):
        return self.linked_lst(indx)


linked_lst = LinkedList()
linked_lst.add_obj(ObjList('Dmitriy'))
linked_lst.add_obj(ObjList('Mandrik'))
linked_lst.add_obj(ObjList('Python'))
linked_lst.remove_obj(2)
linked_lst.add_obj(ObjList('Python OOP'))
n = len(linked_lst)
s = linked_lst(2)
print(n, s)
