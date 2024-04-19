class MaxPooling:
    def __init__(self, step, size):
        self.step = step
        self.size = size

    @classmethod
    def validate_matrix(cls, matrix):
        len_matrix = len(matrix[0])
        for i in matrix:
            if len_matrix != len(i) or not all(type(k) is int for k in i):
                raise ValueError('The first parameter matrix is not in the correct format')

    def __call__(self, matrix, *args, **kwargs):
        self.validate_matrix(matrix)
        m = matrix
        res = []
        sz_v, sz_g = self.size
        sp_v, sp_g = self.step

        for i in range(0, len(m), sp_v):
            if i + sz_v > len(m):
                break
            last_res = []
            for j in range(0, len(m[i]), sp_g):
                lst_1 = []
                if j + sz_g > len(m[i]):
                    break
                for k in range(i, i + sz_v):
                    lst_1 = lst_1 + m[k][j:j+sz_g]
                r = max(lst_1)
                last_res.append(r)
            res.append(last_res)
        return res


mp = MaxPooling(step=(2, 2), size=(2, 2))
res_1 = mp([[1, 2, 3, 4],
            [5, 6, 7, 8],
            [9, 8, 7, 6],
            [5, 4, 3, 2]])

res_2 = mp([[5, 0, 88, 2, 7, 65],
            [1, 33, 7, 45, 0, 1],
            [54, 8, 2, 38, 22, 7],
            [73, 23, 6, 1, 15, 0],
            [4, 12, 9, 1, 76, 6],
            [0, 15, 10, 8, 11, 78]])
print(res_1)
print(res_2)
