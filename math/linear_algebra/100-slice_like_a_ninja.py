#!/usr/bin/env python3
"""
Module to perform slicing on a numpy ndarray along specific axes.
"""


def np_slice(matrix, axes={}):
    """
    Slices a numpy ndarray along specific axes.
    """
    import numpy as np

    slices = [slice(None)] * matrix.ndim

    for axis, slice_tuple in axes.items():
        slices[axis] = slice(*slice_tuple)

    return matrix[tuple(slices)]
