#!/usr/bin/python3
""" This module defines a function called say_my_name"""


def say_my_name(first_name, last_name=""):
    """ A function that prints the given first and last names

    Args:
        first_name(str): the first name
        last_name(str): the last name
    Raises:
        TypeError: If first_name and last_name are not strings

    """
    if not isinstance(first_name, str):
        raise TypeError("first_name must be a string")
    if not isinstance(last_name, str):
        raise TypeError("last_name must be a string")
    print("My name is {} {}".format(first_name, last_name))
