#!/usr/bin/python3
""" A module that defines a function called from_json_string"""

import json


def from_json_string(my_str):
    """ A function that returns the python representation of a json string

    Args:
        my_str: the str to be converted
    Returns:
        the python representation of the string
    """

    return json.loads(my_str)
