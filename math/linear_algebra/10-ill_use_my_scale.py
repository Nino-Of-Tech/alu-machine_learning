#!/usr/bin/env python3
"""
Module for calculating the shape of a numpy.ndarray
"""


def np_shape(matrix):
    """
    Calculates the shape of a numpy.ndarray """
    import numpy as np

    return matrix.shape


# mat1 = np.array([1, 2, 3, 4, 5, 6])
# mat2 = np.array([])
# mat3 = np.array([[[1, 2, 3, 4, 5], [6, 7, 8, 9, 10]],
#                 [[11, 12, 13, 14, 15], [16, 17, 18, 19, 20]]])
# print(np_shape(mat1))
# print(np_shape(mat2))
# print(np_shape(mat3))
