#!/usr/bin/env python3

"""This module contains the function that
updates the learning rate using inverse time decay in numpy
"""

import numpy as np


def learning_rate_decay(alpha, decay_rate, global_step, decay_step):
    """
    updates the learning rate using inverse time decay in numpy
    alpha - is the original learning rate
    decay_rate - weight used to determine rate at which alpha decays
    global_step - number of passes of gradient descent that have elapsed
    decay_step - number of passes of gradient descent that should occur
    before alpha is decayed further
    Returns: the updated value for alpha
    """

    return alpha / (1 + decay_rate * np.floor(global_step / decay_step))
