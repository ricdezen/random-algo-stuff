'''
**Question**: Implement a Priority Queue.

**Explanation**:
- A Queue is a data structure comprised of mainly two methods: `push` and `pop`. The former inserts
  an element into the Queue, while the latter removes it and returns it.
- A Priority Queue guarantees the following:
    1. A pushed element can (must) be assigned a priority.
    2. The popped element will always be the one with the higher priority.

The most basic implementation involves having an array on which you insert elements, while
maintaining ordering over the priority. Every insertion and removal takes `O(n)` time. Removal can
be constant time if the array is managed as a circular queue.

A better implementation involves using a Heap, a binary tree where each node has a certain key, and
a node's children always have keys with a lower value.
A Heap can be easily implemented using an array where, given a node N and its index i, N's children
are situated at indexes 2\\*i+1 and 2\\*i+2.

Both the Priority Queue and the Heap can obviously be implemented to use min logic instead of max
logic.
'''

__author__ = "Riccardo De Zen <riccardodezen98@gmail.com>"

from typing import Any, Tuple, Iterable
from numbers import Real


class PriorityQueue(Iterable[Any]):

    def __init__(self):
        '''
        Constructor, initializes a few useful variables.
        '''
        self._array = list()

    def push(self, priority: Real, item: Any):
        '''
        Insert an item into the Queue.

        Parameters:
            item : Any
                The item to insert into the Queue.

            priority : Real
                The priority for the inserted item.
        '''
        raise NotImplementedError("This is an Abstract class, please extend it.")

    def pop(self) -> Any:
        '''
        Remove an item from the Queue and return it.

        Returns:
            The item in the Queue with the highest priority.
        '''
        raise NotImplementedError("This is an Abstract class, please extend it.")

    def __bool__(self):
        '''
        A Queue is `False` if it's empty and `True` otherwise.
        '''
        return bool(self._array)


class ArrayMaxPQ(PriorityQueue):

    # ! This is the dummy-dum version for practice's sake. You don't want this.

    '''
    Implementation of a PriorityQueue using an array, offering operations in linear time.
    This is a Max Priority Queue, elements with the highest Priority are extracted first.
    '''

    def push(self, priority: Real, item: Any):
        '''
        Insert an item into the Queue.

        Parameters:
            priority : Real
                The priority for the inserted item.

            item : Any
                The item to insert into the Queue.
        '''
        self._array.append((priority, item))
        for i in range(1, len(self._array)):
            if self._array[-i][0] < self._array[-i-1][0]:
                self._swap(-i, -i-1)
            else:
                break

    def pop(self) -> Any:
        '''
        Remove an item from the Queue and return it.

        Returns:
            The item in the Queue with the highest priority.
        '''
        value = self._array[-1]
        del self._array[-1]
        return value[1]

    def _swap(self, i: int, j: int):
        '''
        Swap indices i, j in the list.
        '''
        temp = self._array[i]
        self._array[i] = self._array[j]
        self._array[j] = temp

    def __iter__(self):
        '''
        Return the Queue as a sorted Iterable.
        '''
        for key, value in reversed(self._array):
            yield value


class HeapMaxPQ(PriorityQueue):

    '''
    Implementation of a PriorityQueue using a binary Heap, offering operations in log time.
    This is a Max Priority Queue, elements with the highest Priority are extracted first.
    '''

    def push(self, priority: Real, item: Any):
        '''
        Insert an item into the Queue.

        Parameters:
            priority : Real
                The priority for the inserted item.

            item : Any
                The item to insert into the Queue.
        '''
        self._array.append((priority, item))
        child = len(self._array) - 1
        while True:
            parent = self._up(child)
            if self._array[child][0] > self._array[parent][0]:
                self._swap(child, parent)
                child = parent
            else:
                break

    def pop(self) -> Any:
        '''
        Remove an item from the Queue and return it.

        Returns:
            The item in the Queue with the highest priority.
        '''
        if not self:
            raise Exception("Empty Queue.")

        root = self._array[0]

        if len(self._array) > 1:
            # Ensure more than one element.
            self._swap(0, -1)
            del self._array[-1]
        else:
            # If root was the only element, return.
            del self._array[-1]
            return root[1]

        new = 0
        while True:
            left, right = self._down(new)

            if left is None:
                # No children
                break
            if right is not None:
                # Max key child.
                max_child = left if self._array[left][0] > self._array[right][0] else right
            else:
                max_child = left

            if self._array[max_child][0] > self._array[new][0]:
                # Swap them because the child is bigger than the parent and continue.
                self._swap(new, max_child)
                new = max_child
                continue

            # Already in order
            break

        return root[1]

    def _up(self, index: int) -> int:
        '''
        Find the index of the parent for the given index.
        Going "up" one level in the virtual tree.

        Parameters:
            index : int
                The index for which to find the parent.

        Returns:
            int : The index of the parent. 0 if the index is 0
        '''
        return (index - 1) // 2 if index else 0

    def _down(self, index: int) -> Tuple[int, None]:
        '''
        Go "down" one level in the virtual tree and return the indexes of the children of a node.

        Parameters:
            index : int
                The parent of which we want to know the children.

        Returns:
            Tuple[int, None] : a Tuple of two indexes or None if the index is not valid.
            [0] is the left child, [1] is the right child.
        '''
        left = 2 * index + 1
        right = 2 * index + 2
        return left if left < len(self._array) else None, right if right < len(self._array) else None

    def _swap(self, i: int, j: int):
        '''
        Swap indices i, j in the list.
        '''
        temp = self._array[i]
        self._array[i] = self._array[j]
        self._array[j] = temp

    def __iter__(self):
        '''
        Return the Queue as a sorted list.
        '''
        support = HeapMaxPQ()
        for key, value in self._array:
            support.push(key, value)
        for _ in self._array:
            yield support.pop()
