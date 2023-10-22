#!/usr/bin/env python3
import numpy as np

""" A function that calculates the mean and covariance of a data set """

""" X is a numpy.ndarray of shape (n, d) containing the data set"""


def mean_cov(X):
    X = np.array(X)
    """ n is the number of data points """
    """ d is the number of dimensions in each data point """

    (n, d) = X.shape

    """ If X is not a 2D numpy.ndarray, raise a TypeError
    with the message X must be a 2D numpy.ndarray """
    """ If X.ndim !=2: """

    if X.ndim! = 2:
        raise TypeError("X must be a 2D numpy.ndarray")
    """ If n is less than 2, raise a ValueError
    with the message X must contain multiple data points """

    if n < 2:
        raise ValueError("X must contain multiple data points")
    """Calculate the mean for each dimension: """
    mean = np.mean(X, axis=0, keepdims=True)

    print((X - mean).shape)
    """ Calculate the covariance matrix: """
    """ cov = np.matmul((X - mean).T, X - mean) / (n - 1) """
    sub_x = [i - mean for i in X]
    sum_value = sum([sub_x[i].T*sub_x[i] for i in range(len(X))])
    cov = sum_value/(n-1)

    return mean, cov
