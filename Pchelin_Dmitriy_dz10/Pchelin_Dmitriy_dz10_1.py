class Matrix:

    def __init__(self, matrix_lists):
        self.matrix_lists = matrix_lists

    def __str__(self):
        return '\n'.join(str(i) for i in self.matrix_lists)

    def __add__(self, other):
        return Matrix([[a+b for a, b in zip(my_row, other_row)]
                                 for my_row, other_row in zip(self.matrix_lists, other.matrix_lists)])

l1 = [[1, 2, 3], [4, 5, 6], [7, 8 ,9]]
l2 = [[10, 11, 12], [13, 14, 15], [16, 17, 18]]

matr1 = Matrix(l1)
matr2 = Matrix(l2)
print(matr1, '\n')
print(matr2, '\n')
matr3 = matr1 + matr2
print(matr3, '\n')