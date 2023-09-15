#!/usr/bin/python3
""" This module defines a function called text_indentation"""


def text_indentation(text):
    """ A function that prints a text with 2 new lines
        after each of these characters: ., ? and :
    Args:
        text: the text to be printed
    Raises:
        TypeError: if text is not a string

    """
    if not isinstance(text, str):
        raise TypeError("text must be a string")
    char_set = ['.', '?', ':']
    printable = ""
    for char in text:
        printable += char
        if char in char_set:
            print(printable.strip())
            print("\n", end="")
            printable = ""
    print(printable.strip(), end="")
