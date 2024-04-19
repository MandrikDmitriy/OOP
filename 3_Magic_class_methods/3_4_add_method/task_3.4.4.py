class NewList:
    def __init__(self, lst=None):
        if lst is None:
            self.lst_obj = []
        else:
            self.lst_obj = lst

    def get_list(self):
        return self.lst_obj

    @classmethod
    def __get_difference(cls, obj_1, obj_2):
        for i in obj_2:
            for ind, val in enumerate(obj_1):
                if i == val and type(i) is type(val):
                    obj_1.pop(ind)
        return obj_1

    def __sub__(self, other):
        if not isinstance(other, (list, NewList)):
            raise TypeError("Other object isn't list type or NewList type")

        lst_new = other
        if type(lst_new) is NewList:
            lst_new = other.lst_obj

        return NewList(self.__get_difference(self.lst_obj, lst_new))

    def __isub__(self, other):
        if not isinstance(other, (list, NewList)):
            raise TypeError("Other object isn't list type or NewList type")

        lst_new = other
        if type(lst_new) is NewList:
            lst_new = other.lst_obj

        return NewList(self.__get_difference(self.lst_obj, lst_new))

    def __rsub__(self, other):
        return NewList(self.__get_difference(other, self.lst_obj))


lst1 = NewList([1, 2, -4, 6, 10, 11, 15, False, True])
lst2 = NewList([0, 1, 2, 3, True])
res_1 = lst1 - lst2
print(res_1.get_list())
lst1 -= lst2
print(lst1.get_list())
res2 = lst2 - [0, True]
print(res2.get_list())
res3 = [1, 2, 3, 4.5] - res2
print(res3.get_list())
a = NewList([2, 3])
res4 = [1, 2, 2, 3] - a
print(res4.get_list())
