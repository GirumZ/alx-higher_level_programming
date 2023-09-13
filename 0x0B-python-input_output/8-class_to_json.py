#!/usr/bin/python3
""" A python module that defines a function called class_to_json """


def class_to_json(obj):
    """ a function that returns the dictionary description
        with simple data structure

    Args:
        obj: the given object
    Returns:
        A dictionary description
    """

    return obj.__dict__
