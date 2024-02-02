#!/usr/bin/env python3

"""a function in this module creates
a NN using dropout"""

import tensorflow as tf


def dropout_create_layer(prev, n, activation, keep_prob):
    """prev - tensor with output of previous layer
    n - number of nodes new layer should have
    activation - activation function
    keep_prob - probability that a node is kept
    return output of the new layer"""

    kernel = tf.contrib.layers.variance_scaling_initializer(mode="FAN_AVG")
    layer = tf.layers.Dense(units=n, activation=activation,
                            kernel_initializer=kernel)
    output = tf.layers.Dropout(keep_prob)
    return output(layer(prev))
