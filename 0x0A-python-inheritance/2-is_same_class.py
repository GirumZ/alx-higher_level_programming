#!/usr/bin/python3
""" A module that defines a function called 'is_same_class' """


def is_same_class(obj, a_class):
    """ A function that checks is an object is instance of a class

    Args:
        obj: an object
        a_class: a class
    Returns:
        True if object is an instance of teh class and False if not
    """
    return type(obj) == a_class
