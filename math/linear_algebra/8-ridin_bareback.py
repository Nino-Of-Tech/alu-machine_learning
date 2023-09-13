#!/usr/bin/env python3
"""
Module for performing matrix multiplication
"""


def mat_mul(mat1, mat2):
    """
    Perform matrix multiplication of two 2D matrices.
    """
    if len(mat1[0]) != len(mat2):
        return None
    
    result = [
        [
            sum(a * b for a, b in zip(row, col))
            for col in zip(*mat2)
        ]
        for row in mat1
    ]
    
    return result


if __name__ == "__main__":
    mat1 = [[1, 2], [3, 4], [5, 6]]
    mat2 = [[1, 2, 3, 4], [5, 6, 7, 8]]
    print(mat_mul(mat1, mat2)))
