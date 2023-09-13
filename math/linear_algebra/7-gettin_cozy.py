#!/usr/bin/env python3
"""
Module for concatenating two 2D matrices along a specific axis.
"""


def cat_matrices2D(mat1, mat2, axis=0):
    """ Concatenates two 2D matrices along a specific axis. """
    try:
        if axis == 0:
            if len(mat1[0]) != len(mat2[0]):
                return None
            return [row.copy() for row in mat1] + [row.copy() for row in mat2]
        elif axis == 1:
            if len(mat1) != len(mat2):
                return None
            return [r1 + r2 for r1, r2 in zip(mat1, mat2)]
    except IndexError:
        return None


if __name__ == "__main__":
    mat1 = [[1, 2], [3, 4]]
    mat2 = [[5, 6]]
    mat3 = [[7], [8]]
    mat4 = cat_matrices2D(mat1, mat2)
    mat5 = cat_matrices2D(mat1, mat3, axis=1)
    print(mat4)
    print(mat5)
    mat1[0] = [9, 10]
    mat1[1].append(5)
    print(mat1)
    print(mat4)
    print(mat5)
