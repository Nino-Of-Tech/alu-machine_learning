#!/usr/bin/env python3

from copy import deepcopy


def add_matrices(mat1, mat2):
    """
    Adds two matrices of the same shape element-wise.
    """
    if not isinstance(mat1, list) or not isinstance(mat2, list):
        return None

    if len(mat1) != len(mat2):
        return None

    result = deepcopy(mat1)

    for i in range(len(mat1)):
        if isinstance(mat1[i], list):
            if not isinstance(mat2[i], list) or len(mat1[i]) != len(mat2[i]):
                return None
            result[i] = add_matrices(mat1[i], mat2[i])
            if result[i] is None:
                return None
        else:
            result[i] = mat1[i] + mat2[i]

    return result


# Testing
mat1 = [1, 2, 3]
mat2 = [4, 5, 6]
print(add_matrices(mat1, mat2))

mat1 = [[1, 2], [3, 4]]
mat2 = [[5, 6], [7, 8]]
print(add_matrices(mat1, mat2))
