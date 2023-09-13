#!/usr/bin/python3
""" A class defination of Student """


class Student:
    """ A class called Student"""

    def __init__(self, first_name, last_name, age):
        """ A constractor method for the Student class

        Args:
            first_name: the first name of a person instance
            last_name: the last_name of a person instance
            age: the age of a person instance
        """

        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """ A method that retrieves a dictionary representation
            of a Student instance
        Returns:
            the dictionary representation of a Student instance
        """

        return self.__dict__
