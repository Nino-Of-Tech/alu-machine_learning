#!/usr/bin/env python3

"""a function in this module calculates
cost of a neural network with L2 regularization"""

import numpy as np


def l2_reg_gradient_descent(Y, weights, cache, alpha, lambtha, L):
    """updates weights and biases of a NN using gradient descent
    Y - one-hot of shape (classes, m) has
    labels for data
        classes - no. of classes
        m - no. of data points
    weights - dict of weights & biases of a NN
    cache - dict of outputs of each layer of NN
    alpha - learning rate
    lambtha - L2 regularization param
    L - number of layers of the network
    NN uses tanh activations but last layer uses softmax"""

    # w = (1 - alpha(lambtha/m)) * w - alpha( der(cost) / der(w) )

    m = Y.shape[1]
    for i in range(L, 0, -1):
        A = cache['A' + str(i)]
        A_prev = cache['A' + str(i - 1)]
        W = weights['W' + str(i)]
        b = weights['b' + str(i)]
        if i == L:
            dZ = A - Y
        else:
            dZ = dA * (1 - (A ** 2))
        dW = (1 / m) * np.matmul(dZ, A_prev.T) + ((lambtha / m) * W)
        db = (1 / m) * np.sum(dZ, axis=1, keepdims=True)
        dA = np.matmul(W.T, dZ)
        weights['W' + str(i)] = W - (alpha * dW)
        weights['b' + str(i)] = b - (alpha * db)
    return weights
