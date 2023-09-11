#!/usr/bin/python3
""" A module that defines a class called 'BaseGeometry'"""


class BaseGeometry:
    """ A class called BaseGeometry"""

    def area(self):
        """ A public instance method that computes the area of an instance
        Raises:
            Excepsion: Always
        """
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """ A public instance method that validates a value

        Args:
            name: Name
            value: Value
        Raises:
            TypeError: if value is not integer
            ValueError: if value is less or equal to 0
        """
        if not type(value) == int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
