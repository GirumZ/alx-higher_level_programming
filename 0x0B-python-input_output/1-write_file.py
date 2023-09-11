#!/usr/bin/python3
""" A module defining a function called write_file"""


def write_file(filename="", text=""):
    """ A function that writes on a file

    Args:
        filename: the path to the file to be written on
        text: the string to be written
    Return:
        The number of characters written
    """

    with open(filename, "w", encoding="utf-8") as f:
        written = f.write(text)
        return (written)
