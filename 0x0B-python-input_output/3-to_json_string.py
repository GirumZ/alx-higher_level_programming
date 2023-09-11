#!/usr/bin/python3
""" A module that defines a function called to_json_string"""

import json


def to_json_string(my_obj):
    """ A function that returns the json representation of an object

    Args:
        my_obj: the object to be converted
    Returns:
        the json representation of the object
    """

    x = json.dumps(my_obj)
    return x
