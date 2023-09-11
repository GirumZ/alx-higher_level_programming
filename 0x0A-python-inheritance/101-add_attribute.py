#!/usr/bin/python3
""" A module that defines a function called add_attribute"""


def add_attribute(obj, attr, value):
    """ Asses a new attribute if possible.

    Args:
        obj: the object for the attribute to be added
        attr: the new attribute
        value: the value of the attribute

    Raises:
        TypeError: If the new attribute can not be added.
    """

    if not hasattr(obj, "__dict__"):
        raise TypeError("can't add new attribute")
    setattr(obj, attr, value)
