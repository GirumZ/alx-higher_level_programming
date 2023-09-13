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

    def to_json(self, attrs=None):
        """ A method that retrieves a dictionary representation
            of a Student instance
        Returns:
            the dictionary representation of a Student instance
        """

        new_dict = {}
        if type(attrs) == list:
            for item in attrs:
                if type(item) == str and item in self.__dict__:
                    new_dict[item] = self.__dict__[item]
            return new_dict
        return self.__dict__

    def reload_from_json(self, json):
        """ A method that reloads the attribute dictionary

        Args:
            json: A new dictionary of attributes
        """
        for key in json:
            setattr(self, key, json[key])
