__author__ = "Riccardo De Zen <riccardodezen98@gmail.com>"

import unittest
from typing import List
from numpy.random import rand
from parameterized import parameterized, parameterized_class

from ..priority_queue import ArrayMaxPQ, HeapMaxPQ


@parameterized_class(("pq_class",), [
    (ArrayMaxPQ,),
    (HeapMaxPQ,)
])
class TestPriorityQueue(unittest.TestCase):

    def setUp(self):
        '''
        Create the Queue.
        '''
        self.queue = self.pq_class()

    @parameterized.expand([
        (list(rand(10)), list(rand(10))),
        (list(rand(100)), list(rand(100))),
        (list(-x for x in rand(100)), list(-x for x in rand(100)))
    ])
    def test_random_values(self, values: List, priorities: List):
        '''
        Parameters:
            values : List
                The values to insert in the List.

            priorities : List
                The priorities. Only the first `len(values)` items will be used.
        '''

        items = [(priorities[i], values[i]) for i in range(len(values))]

        for item in items:
            self.queue.push(*item)

        result = list()
        while self.queue:
            result.append(self.queue.pop())

        expected = [x[1] for x in reversed(sorted(items, key=lambda x: x[0]))]

        self.assertListEqual(result, expected)

    @parameterized.expand([
        (list(rand(10)), list(rand(10))),
        (list(rand(100)), list(rand(100))),
        (list(-x for x in rand(100)), list(-x for x in rand(100)))
    ])
    def test_iter(self, values: List, priorities: List):
        '''
        Ensure iter yields in the expected order.

        Parameters:
            values : List
                The values to insert in the List.

            priorities : List
                The priorities. Only the first `len(values)` items will be used.
        '''
        items = [(priorities[i], values[i]) for i in range(len(values))]

        for item in items:
            self.queue.push(*item)

        result = list(self.queue)

        expected = [x[1] for x in reversed(sorted(items, key=lambda x: x[0]))]

        self.assertListEqual(result, expected)
