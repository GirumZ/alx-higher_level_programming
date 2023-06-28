#!/usr/bin/python3
"""Defination of class 'Square' with privet instance attribute"""


class Square:
    """Class Square that defines a square.
    """
    def __init__(self, size=0):
        """Inits Square with privet instance attribute 'size'

        Args:
            size: Size of the square with integer value

        Raises:
            TypeError: When size is not integer
            ValueError: When size is negative
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

    def area(self):
        """Calculates the area of a square"""
        return self.__size * self.__size
