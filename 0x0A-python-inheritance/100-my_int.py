#!/usr/bin/python3
""" A module that creates a MyInt class"""


class MyInt(int):
    """ A class called MyInt inheriting the int class"""

    def __eq__(self, other):
        """ Method returning != """
        return not int.__eq__(self, other)

    def __ne__(self, other):
        """ Method returning == """
        return not int.__ne__(self, other)
