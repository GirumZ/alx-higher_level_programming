#!/usr/bin/python3
""" A module that defines a function called 'is_kind_of_class' """


def is_kind_of_class(obj, a_class):
    """ A function that checks is an object is instance of a class
        or if the object is an instance of a class that inherited from,
        the specified class

    Args:
        obj: an object
        a_class: a class
    Returns:
        True if object is an instance of teh class and False if not
    """
    return isinstance(obj, a_class)
