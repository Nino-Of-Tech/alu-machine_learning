#!/usr/bin/env python3
"""
Module for concatenating two arrays.
"""


def cat_arrays(arr1, arr2):
    """
    Concatenates two arrays into a single array.
    """
    return arr1 + arr2


if __name__ == "__main__":
    arr1 = [1, 2, 3, 4, 5]
    arr2 = [6, 7, 8]
    print(cat_arrays(arr1, arr2))
    print(arr1)
    print(arr2)
