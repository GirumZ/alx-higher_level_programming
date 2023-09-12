#!/usr/bin/python3
""" A module that defines a function called save_to_json_file.py"""


import json


def save_to_json_file(my_obj, filename):
    """ A function that  writes an Object to a
        text file, using a JSON representation
    Args:
        my_obj: the object
        filename: the path to the file to be written on
    """

    with open(filename, "w", encoding="utf-8") as f:
        json.dump(my_obj, f)
