#!/usr/bin/python3
""" A module that defines a function called add_integer"""


def add_integer(a, b=98):
    """ Calculates the sum of two numbers

    Args:
        a: the first number
        b: the second number
    Raises:
        TypeError: If a or b is not an integer or a float
    Returns:
        The sum of the two numbers
    """

    if not (isinstance(a, (int, float))):
        raise TypeError("a must be an integer")
    elif not (isinstance(b, (int, float))):
        raise TypeError("b must be an integer")
    a = int(a)
    b = int(b)
    return a + b
