class TreeObj:
    def __init__(self, indx, value=None):
        self.indx = indx
        self.value = value
        self.__left = self.__right = None

    @property
    def left(self):
        return self.__left

    @left.setter
    def left(self, val):
        self.__left = val

    @property
    def right(self):
        return self.__right

    @right.setter
    def right(self, val):
        self.__right = val


class DecisionTree:
    @classmethod
    def predict(cls, root, x):
        pass

    @classmethod
    def add_obj(cls, obj, node=None, left=True):
        pass
