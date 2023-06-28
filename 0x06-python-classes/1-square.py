#!/usr/bin/python3
"""Defination of class 'Square' with privet instance attribute"""


class Square:
    """Class Square that defines a square.
    """
    def __init__(self, size=0):
        """Inits Square with privet instance attribute 'size'

        Args:
            size: Size of the square with integer value
        """
        self.__size = size
