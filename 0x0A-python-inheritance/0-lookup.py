#!/usr/bin/python3
""" A module that defines a function called lookup """


def lookup(obj):
    """ A function that returns the methods and attributes of an object

    Args:
        obj: an object
    Returns:
        the methods and attributes related with the given object
    """

    return dir(obj)
