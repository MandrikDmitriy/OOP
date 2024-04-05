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
        obj = root
        while obj:
            obj_next = cls.get_next(obj, x)
            if obj_next is None:
                break
            obj = obj_next
        return obj.value

    @classmethod
    def get_next(cls, obj, x):
        if x[obj.indx] == 1:
            return obj.left
        return obj.right

        # next_root = root
        # if x[0] == 1:
        #     for i in [0, 1]:
        #         if x[i] == 1:
        #             next_root = next_root.left
        #         else:
        #             next_root = next_root.right
        # else:
        #     for i in [0, 2]:
        #         if x[i] == 1:
        #             next_root = next_root.left
        #         else:
        #             next_root = next_root.right
        # return next_root.value

    @classmethod
    def add_obj(cls, obj, node=None, left=True):
        if node:
            if left:
                node.left = obj
            else:
                node.right = obj
        return obj


root = DecisionTree.add_obj(TreeObj(0))
v_11 = DecisionTree.add_obj(TreeObj(1), root)
v_12 = DecisionTree.add_obj(TreeObj(2), root, False)
DecisionTree.add_obj(TreeObj(-1, 'will be programmer'), v_11)
DecisionTree.add_obj(TreeObj(-1, 'will be coder'), v_11, False)
DecisionTree.add_obj(TreeObj(-1, 'not all is lost'), v_12)
DecisionTree.add_obj(TreeObj(-1, 'you loser'), v_12, False)

x = [0, 1, 1]
res = DecisionTree.predict(root, x)
print(res)
