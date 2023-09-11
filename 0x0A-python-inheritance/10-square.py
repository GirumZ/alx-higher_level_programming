#!/usr/bin/python3
""" A module defining a  class called Square that
    inherits the Rectangle class"""


Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """ A class that inherits a class called Rectangle"""

    def __init__(self, size):
        """ A creator method that initializis a Square instance

        Args:
            size: size of the square
        """
        self.integer_validator("size", size)
        super().__init__(size, size)
        self.__size = size
