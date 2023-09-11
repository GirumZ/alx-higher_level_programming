#!/usr/bin/python3
""" A module that defines a class called 'BaseGeometry'"""


BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """ A Rectangle class that is a subclass of BaseGeometry class"""

    def __init__(self, width, height):
        """ A creator method that initializes a class instance

        Args:
            width: the width of a Rectangle instance
            height: the height of a Rectangle instance
        """
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height
