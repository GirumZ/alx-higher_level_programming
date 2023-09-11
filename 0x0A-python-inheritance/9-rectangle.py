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

    def area(self):
        """ A method to calculate the area of a Rectangle instance

        Returns:
             the computed area
        """

        return self.__width * self.__height

    def __str__(self):
        """ Displays a Rectangle instance in a specified format"""

        return "[Rectangle] {:d}/{:d}".format(self.__width, self.__height)
