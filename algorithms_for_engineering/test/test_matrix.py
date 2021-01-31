__author__ = "Riccardo De Zen <riccardodezen98@gmail.com>"

import unittest
import numpy.testing

from parameterized import parameterized
from algorithms_for_engineering.matrix import Matrix, matrix_sum, matrix_product_naive, matrix_fractal_product


class TestMatrix(unittest.TestCase):

    @parameterized.expand([[Matrix(10, 10, 'random'), Matrix(10, 10, 'random')] for _ in range(10)])
    def test_matrix_sum(self, A: Matrix, B: Matrix):
        '''
        Compares operations with `numpy`, which we assume as correct.
        '''
        numpy.testing.assert_array_equal(
            matrix_sum(A, B)._matrix, A._matrix + B._matrix
        )

    @parameterized.expand([[Matrix(10, 10, 'random'), Matrix(10, 10, 'random')] for _ in range(10)])
    def test_matrix_product_naive(self, A: Matrix, B: Matrix):
        '''
        Compares operations with `numpy`, which we assume as correct.
        '''
        numpy.testing.assert_array_equal(
            matrix_product_naive(A, B)._matrix, A._matrix @ B._matrix
        )

    @parameterized.expand([[Matrix(16, 16, 'random'), Matrix(16, 16, 'random')] for _ in range(10)])
    def test_matrix_product_fractal(self, A: Matrix, B: Matrix):
        '''
        Compares operations with `numpy`, which we assume as correct.
        '''
        numpy.testing.assert_array_equal(
            matrix_fractal_product(A, B)._matrix, A._matrix @ B._matrix
        )
