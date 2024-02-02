#!/usr/bin/env python3

"""the function in this module calculates
cost of  a neural network with L2 regularization"""


def l2_reg_cost(cost, lambtha, weights, L, m):
    """returns cost of the network accounting
    for L2 regularization
    cost - cost of network without L2
    lambtha regularization param
    weights - dict of weights & biases of the nn
    L - number of layers in NN
    m - number of data points used"""

    # cf = cost + lambda / 2*m * sum(//w//**2)
    l2_penalty = 0
    for layer in range(1, L+1):
        l2_penalty += (weights['W{}'.format(layer)] ** 2).sum()

    l2_cost = cost + (lambtha / (2*m)) * l2_penalty

    return l2_cost
