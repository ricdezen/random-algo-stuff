'''
Small 2D matrix class to wrap numpy arrays in order to have to implement things myself.
'''
import numpy
import numpy.random
from typing import Union


class Matrix():

    def __init__(self, rows: int, columns: int, content: Union[int, str] = 0):
        '''
        Create a new 2D matrix filled with zeros.

        Parameters:
            rows : int
                Number of rows.

            columns : int
                Number of columns.

            content : int
                Value to put or 'random' for random 32 bit integers.

            **kwargs : dict
                Arguments for `numpy.random.randint` or `numpy.full` method.
        '''
        super().__init__()
        if content == 'random':
            ii32 = numpy.iinfo(numpy.int32)
            self._matrix = numpy.random.randint(ii32.min, ii32.max, (rows, columns))
        self._matrix = numpy.full((rows, columns), content)

        self._rows = rows
        self._columns = columns

    def __getitem__(self, index):
        return self._matrix[index]

    def __setitem__(self, index, value):
        self._matrix[index] = value

    @property
    def rows(self) -> int:
        return self._rows

    @property
    def columns(self) -> int:
        return self._columns


def matrix_sum(A: Matrix, B: Matrix) -> Matrix:

    if A.rows != B.rows or A.columns != B.columns:
        raise ValueError("Matrices must have the same size.")

    C = Matrix(A.rows, A.columns)
    for i in range(A.rows):
        for j in range(A.columns):
            C[i, j] = A[i, j] + B[i, j]
    return C


def matrix_product_naive(A: Matrix, B: Matrix) -> Matrix:
    return
