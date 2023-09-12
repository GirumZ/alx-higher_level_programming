#!/usr/bin/python3
""" A module that defines a function called load_from_json_file"""


import json


def load_from_json_file(filename):
    """ A function that creates an object from a JSON file

    Args:
        filename: path to the file
    """

    with open(filename, "r", encoding="utf-8") as f:
        data = json.load(f)
        return data
