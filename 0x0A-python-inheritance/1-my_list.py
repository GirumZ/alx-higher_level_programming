#!/usr/bin/python3
""" A module that creates a class called MyList """


class MyList(list):
    """ Defines a class called Mylist """

    def print_sorted(self):
        """ A public instance method that prints a sorted list"""

        copy_list = self.copy()
        copy_list.sort()
        print(copy_list)
