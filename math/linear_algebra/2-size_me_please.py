#!/usr/bin/env python3

''' Calculates the shape of a matrix '''

def matrix_shape(matrix):
    ''' Check for matrix and return the shape '''

    shape = []

    while type(matrix) == list:
        shape.append(len(matrix))
        matrix = matrix[0]
    return shape
