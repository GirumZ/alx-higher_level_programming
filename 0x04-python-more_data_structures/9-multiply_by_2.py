#!/usr/bin/python3
def multiply_by_2(a_dictionary):
    new_dictionary = {x: 2 * y for x, y in a_dictionary.items()}
    return (new_dictionary)
