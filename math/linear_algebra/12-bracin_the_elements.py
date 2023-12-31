#!/usr/bin/env python3
"""
Module to perform element-wise operations on numpy.ndarrays
"""


def np_elementwise(mat1, mat2):
    """
    Performs element-wise addition, subtraction, multiplication, and division.
    """
    import numpy as np

    add = np.add(mat1, mat2)
    sub = np.subtract(mat1, mat2)
    mul = np.multiply(mat1, mat2)
    div = np.divide(mat1, mat2)
    return (add, sub, mul, div)
