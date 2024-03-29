#!/usr/bin/python3
""" This module creates an empty class Rectangle that defines a rectangle"""


class Rectangle:
    """ An empty class called Rectangle"""

    def __init__(self, width=0, height=0):
        """ A method to initialize instances

        Args:
            width: the width of a rectangle instance
            height: the height of a rectangle instance
        Raises:
            TypeError: if width or height is not integers
            ValueError: if width or height is less than 0
        """

        if not isinstance(width, int):
            raise TypeError("width must be an integer")
        if not isinstance(height, int):
            raise TypeError("width must be an integer")
        if width < 0:
            raise ValueError("width must be >= 0")
        if height < 0:
            raise ValueError("width must be >= 0")

        self.__width = width
        self.__height = height

    @property
    def width(self):
        """ A method to retrive the width

        Returns:
            the width
        """

        return self.__width

    @width.setter
    def width(self, value):
        """ A method to set the width

        Args:
            value: the value to be set
        Raises:
            TypeError: If width is not an integer
            ValueError: If width is less than 0
        """

        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """ A method to retrive the height

        Returns:
            the height
        """

        return self.__height

    @height.setter
    def height(self, value):
        """ A method to set the height

        Args:
            value: the value to be set
        Raises:
            TypeError: If height is not an integer
            ValueError: If height is less than 0
        """

        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")

        self.__height = value

    def area(self):
        """ A module that calculates the area of a rectangle instance"""

        return self.__width * self.__height

    def perimeter(self):
        """ A module that calculates the perimeter of a rectangle instance"""
        if self.__width == 0 or self.__height == 0:
            return 0
        return (2 * (self.__width + self.__height))
