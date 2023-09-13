#!/usr/bin/env python3
"""
The function add_matrices2D that adds two 2D matrices element-wise.
"""


def add_matrices2D(mat1, mat2):
    """
    Adds two 2D matrices element-wise and returns a new matrix.
    """
    if len(mat1) != len(mat2) or any(len(row1) != len(row2) for row1,
                                                  row2 in zip(mat1, mat2)):
        return None

    return [[a + b for a, b in zip(row1, row2)] for row1, row2 in zip
            (mat1, mat2)]


if __name__ == "__main__":
    mat1 = [[1, 2], [3, 4]]
    mat2 = [[5, 6], [7, 8]]
    print(add_matrices2D(mat1, mat2))
    print(mat1)
    print(mat2)
    print(add_matrices2D(mat1, [[1, 2, 3], [4, 5, 6]]))
