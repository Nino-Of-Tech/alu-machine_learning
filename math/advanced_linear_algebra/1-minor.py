#!/usr/bin/env python3

""" Module for calculating the minor of a matrix from a determinant """


def determinant(matrix):
    """
    Calculates the determinant of a matrix
    """
    # Check if matrix is a list of lists
    if not isinstance(matrix, list) or
    not all(isinstance(row, list) for row in matrix):
        raise TypeError("matrix must be a list of lists")

    # Check for an empty matrix [[]]
    if len(matrix) == 1 and len(matrix[0]) == 0:
        return 1

    # Check for a non-square matrix
    if any(len(row) != len(matrix) for row in matrix):
        raise ValueError("matrix must be a square matrix")

    # Base case: 1x1 matrix
    if len(matrix) == 1:
        return matrix[0][0]

    # Base case: 2x2 matrix
    if len(matrix) == 2:
        return matrix[0][0] * matrix[1][1] - matrix[0][1] * matrix[1][0]

    # Recursive case for a matrix of size 3x3 or larger
    det = 0
    for j in range(len(matrix)):
        cofactor = ((-1) ** j) * matrix[0][j] * determinant(
                [row[:j] + row[j+1:] for row in matrix[1:]])
        det += cofactor

    return det


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
