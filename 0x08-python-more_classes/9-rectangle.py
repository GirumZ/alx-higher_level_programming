#!/usr/bin/python3
""" This module creates an empty class Rectangle that defines a rectangle"""


class Rectangle:
    """ A Rectangle class with width and height

    Attribute:
        number_of_instances: the number of Rectangle instances
        print_symbol: a symbol for Rectangle object representation
    """

    number_of_instances = 0
    print_symbol = "#"

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
        Rectangle.number_of_instances += 1

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

    def __str__(self):
        """ A module that formaats the output of print() and str()

        Returns:
            empty string if width or height is 0 otherwise a rectangle shape
        """
        rec_shape = ""
        if self.__width == 0 or self.__height == 0:
            return rec_shape
        if self.print_symbol:
            symbol = "{}".format(self.print_symbol)
        else:
            symbol = "{}".format(Rectangle.print_symbol)
        for i in range(self.__height):
            for j in range(self.__width):
                rec_shape += symbol
            rec_shape += "\n"
        return rec_shape[:-1]

    def __repr__(self):
        """ A method to format the output of repr() function

        Returns:
            the string representation of an object
        """
        return "Rectangle({:d}, {:d})".format(self.__width, self.__height)

    def __del__(self):
        """ Prints a given message at object deletion"""
        print("Bye rectangle...")
        Rectangle.number_of_instances -= 1

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        """ Compares two rectangles
        Return:
            the bigger rectangle
        """

        if not isinstance(rect_1, Rectangle):
            raise TypeError("rect_1 must be an instance of Rectangle")
        if not isinstance(rect_2, Rectangle):
            raise TypeError("rect_2 must be an instance of Rectangle")
        if rect_2.area() > rect_1.area():
            return rect_2
        return rect_1

    @classmethod
    def square(cls, size=0):
        """ Creates a square using the rectangle class"""
        return Rectangle(size, size)
