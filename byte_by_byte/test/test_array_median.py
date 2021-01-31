__author__ = "Riccardo De Zen <riccardodezen98@gmail.com>"

import numpy
import unittest

from numbers import Number
from typing import Sequence
from numpy.random import rand
from parameterized import parameterized

from byte_by_byte.array_median import median


class TestArrayMedian(unittest.TestCase):

    @parameterized.expand([
        # Even size.
        [list(rand(10)), list(rand(10))],
        # Odd size.
        [list(rand(99)), list(rand(10))]
    ])
    def test_array_median(self, first: Sequence[Number], second: Sequence[Number]):
        '''
        Compares the `median` method to the `numpy` version, which we assume as correct.

        Parameters:
            first: Sequence[Number]
                First of the two arrays, must be sorted.

            second: Sequence[Number]
                Second of the two arrays, must be sorted.

        '''
        first.sort()
        second.sort()

        self.assertEqual(median(first, second), numpy.median(first + second))
