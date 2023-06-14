#!/usr/bin/python3
def complex_delete(a_dictionary, value):
    key_list = list(a_dictionary.keys())
    for values in key_list:
        if a_dictionary.get(values) == value:
            del a_dictionary[values]
    return (a_dictionary)
