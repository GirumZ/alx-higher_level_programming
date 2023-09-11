#!/usr/bin/python3
""" A module that defines a function called 'inherits_from.py' """


def inherits_from(obj, a_class):
    """ A function that checks if the object is an instance of a class
        that inherited (directly or indirectly) from the specified class

    Args:
        obj: an object
        a_class: a class
    Returns:
        True if object is an instance of the class that
        inherited from the specified class and False if not
    """
    return isinstance(obj, a_class) and type(obj) != a_class
