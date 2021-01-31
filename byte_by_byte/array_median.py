'''
**Question**: Find the median of two sorted arrays.

**Explanation**: Given an array of length `n`, its median is the `n/2` smallest element in the array
if `n` is odd, and the average of the `n/2` and `(n-1)/2` elements if `n` is even.
The two arrays are merged into one while keeping the ordering and then the median is computed on the
resulting array.
'''

__author__ = "Riccardo De Zen <riccardodezen98@gmail.com>"

from typing import Sequence
from numbers import Number


def median(first: Sequence[Number], second: Sequence[Number]) -> Number:
    '''
    Find the median of two sorted arrays.

    Parameters:
        first : Sequence[Number]
            The first of the two arrays. Must be sorted.

        second : Sequence[Number]
            The second of the two arrays. Must be sorted.

    Returns:
        Number : The median of the two arrays.
    '''
    # The two arrays must be merged into one, remaining sorted.
    n = len(first)
    m = len(second)
    i = 0
    j = 0
    merged = [0] * (n + m)
    # Scan the two arrays, and put the smallest element in `merged`.
    while i < n and j < m:
        if first[i] > second[j]:
            merged[i + j] = second[j]
            j += 1
        else:
            merged[i + j] = first[i]
            i += 1
    # If j reached m, add any leftovers from `first`.
    while i < n:
        merged[i + j] = first[i]
        i += 1
    # If i reached n, add any leftovers from `second`.
    while j < m:
        merged[i + j] = second[j]
        j += 1

    size = n + m
    # If size is odd return the middle element, otherwise the average of the two middle elements.
    return merged[size // 2] if size % 2 else (merged[size // 2] + merged[(size - 1) // 2]) / 2
