#!/usr/bin/env python3

""" Module to calculate the minor of a matrix from determinant """

determinant = __import__('0-determinant').determinant


def minor(matrix):
    """
    Calculates the minor matrix of a matrix
    """

    # Check if matrix is a list of lists
    if not isinstance(matrix, list) or not all(isinstance(
     row, list) for row in matrix):
        raise TypeError("matrix must be a list of lists")

    # Check for an empty or non-square matrix
    if len(matrix) == 0 or any(len(row) != len(matrix) for row in matrix):
        raise ValueError("matrix must be a non-empty square matrix")

    # For a 1x1 matrix
    if len(matrix) == 1:
        return [[1]]

    minors = []
    for i in range(len(matrix)):
        minor_row = []
        for j in range(len(matrix)):
            sub_matrix = [row[:j] + row[j+1:] for idx, row in enumerate(
                matrix) if idx != i]
            minor_val = determinant(sub_matrix)
            minor_row.append(minor_val)
        minors.append(minor_row)

    return minors
