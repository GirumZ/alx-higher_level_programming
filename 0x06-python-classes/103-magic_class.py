#!/usr/bin/python3
""" class defination of MagicClass"""
import math


class MagicClass():
    """class defination of MagicClass"""
    def __init__(self, radius):
        """ constructor"""

        self._MagicClass__radius = 0

        if type(radius) is not int or type(radius) is not float:
            raise TypeError("radius must be a number")

        self._MagicClass__radius = radius

    def area(self):
        """ method for calculating area"""
        return self._MagicClass_radius ** 2 * math.pi

    def circumference(self):
        """ method to calculate circumference"""
        return 2 * math.pi * self._MagicClass__radius
