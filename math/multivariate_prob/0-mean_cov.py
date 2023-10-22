#!/usr/bin/env python3
import numpy as np

""" A function that calculates the mean and covariance of a data set """

""" X is a numpy.ndarray of shape (n, d) containing the data set """

def mean_cov(x):
    """
    calculate mean and covariance of a data set
    x - numpy.ndarray - data set, shape (n, d)
    n - int - number of data points
    d - int - number of dimensions
    """
    if not isinstance(x, np.ndarray) or len(x.shape) != 2:
        raise TypeError("X must be a 2D numpy.ndarray")

    x = np.array(x)
    if x.shape[0] < 2:
        raise ValueError("X must contain multiple data points")

    return mean, cov
