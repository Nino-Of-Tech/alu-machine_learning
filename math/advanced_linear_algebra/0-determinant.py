#!/usr/bin/env python3
def determinant(matrix):
    """
    Calculates the determinant of a matrix

    Args:
        matrix (list of lists): Matrix of
        which the determinant should be calculated.

    Returns:
        float: Determinant of the matrix.

    Raises:
        TypeError: If matrix is not a list of lists.
        ValueError: If matrix is not a square matrix.

    """

    # Check if matrix is a list of lists
    if not isinstance(matrix, list) or not
    all(isinstance(row, list) for row in matrix):
        raise TypeError("matrix must be a list of lists")

    # Check for an empty matrix [[]]
    if len(matrix) == 1 and len(matrix[0]) == 0:
        return 1

    # Check for a non-square matrix
    if len(matrix) != len(matrix[0]):
        raise ValueError("matrix must be a square matrix")

    # Base case: 1x1 matrix
    if len(matrix) == 1 and len(matrix[0]) == 1:
        return matrix[0][0]

    # Base case: 2x2 matrix
    if len(matrix) == 2 and len(matrix[0]) == 2:
        return matrix[0][0] * matrix[1][1] - matrix[0][1] * matrix[1][0]

    # Recursive case for a matrix of size 3x3 or larger
    det = 0
    for j in range(len(matrix)):
        # Compute the cofactor
        cofactor = ((-1) ** j) * matrix[0][j] * determinant(
                [row[:j] + row[j+1:] for row in matrix[1:]])
        det += cofactor

    return det
