#!/usr/bin/env python3
"""coefficient of the derivative of the polynomial"""


def poly_derivative(poly):
    """derivative of the polynomial
    """
    if not poly or type(poly) is not list or not all
    (isinstance(i, (int, float)) for i in poly):
        return None  # check if poly is a valid list of numbers

    derivative = [poly[i] * i for i in range(1, len(poly))]
    # apply the power rule for each term

    while derivative and derivative[-1] == 0:
        derivative.pop()

    return derivative if derivative else [0]
