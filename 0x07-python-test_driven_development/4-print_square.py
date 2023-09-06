#!/usr/bin/python3
""" This module defines a function called print_square"""


def print_square(size):
    """ A function that prints a square with the # character

    Args:
        size(int): the length of the square
    Raises:
        TypeError: If size is not an integer.
        TypeError: If size is a float and is less than 0
        ValueError: If size is less than 0

    """

    if isinstance(size, float) and size < 0:
        raise TypeError("size must be an integer")
    if not isinstance(size, int):
        raise TypeError("size must be an integer")
    if isinstance(size, int) and size < 0:
        raise ValueError("size must be >= 0")
    for line in range(size):
        for character in range(size):
            print("#", end="")
        print("")
