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
        else:
            self._matrix = numpy.full((rows, columns), content, dtype=object)

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
    '''
    Raises:
        ValueError : if the sizes of A and B are different.
    '''

    if A.rows != B.rows or A.columns != B.columns:
        raise ValueError("Matrices must have the same size.")

    C = Matrix(A.rows, A.columns)
    for i in range(A.rows):
        for j in range(A.columns):
            C[i, j] = A[i, j] + B[i, j]
    return C


def matrix_product_naive(A: Matrix, B: Matrix) -> Matrix:
    '''
    Naive iterative matrix multiplication algorithm.

    Raises:
        ValueError : if A.columns != B.rows.
    '''

    if A.columns != B.rows:
        raise ValueError(f"A.columns ({A.columns}) != B.rows ({B.rows}).")

    C = Matrix(A.rows, B.columns)
    for i in range(A.rows):
        for j in range(B.columns):
            C[i, j] = A[i, 0] * B[0, j]
            for k in range(1, A.columns):
                C[i, j] += A[i, k] * B[k, j]

    return C


def matrix_fractal_product(A: Matrix, B: Matrix) -> Matrix:
    '''
    This algorithm works only on square Matrices of size 2^n for some n.

    Raises:
        ValueError : if the Matrices are not squared matrices of size 2^n.
    '''

    if A.rows != A.columns or A.rows != B.rows or A.columns != B.columns:
        raise ValueError("Matrices are not equal sized and squared.")

    n = A.rows
    if not ((n & (n-1) == 0) and n != 0):
        raise ValueError("Matrix A is not of size 2^n.")

    C = Matrix(n, n)
    h = n // 2
    if n == 1:
        return A[0, 0] * B[0, 0]

    A11, A12, A21, A22 = A[:h, :h], A[:h, h:], A[h:, :h], A[h:, h:]
    B11, B12, B21, B22 = B[:h, :h], B[:h, h:], B[h:, :h], B[h:, h:]

    # C11
    C[:h, :h] = matrix_sum(
        matrix_fractal_product(A11, B11),
        matrix_fractal_product(A12, B21)
    )
    # C12
    C[:h, h:] = matrix_sum(
        matrix_fractal_product(A11, B12),
        matrix_fractal_product(A12, B22)
    )
    # C21
    C[h:, :h] = matrix_sum(
        matrix_fractal_product(A21, B11),
        matrix_fractal_product(A22, B21)
    )
    # C22
    C[h:, h:] = matrix_sum(
        matrix_fractal_product(A21, B12),
        matrix_fractal_product(A22, B22)
    )

    return C
