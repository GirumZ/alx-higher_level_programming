#!/usr/bin/python3
""" A module that defines a Base class"""
import json
import os.path


class Base:
    """ Defination of a Base class"""

    __nb_objects = 0

    def __init__(self, id=None):
        """ Constructer function for the Base class
        Args:
            id: identification number for class instances
        """

        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """ A method that returns json representation of a list
        Returns:
            the json representation of a list
        """
        if list_dictionaries is None or list_dictionaries == "[]":
            return "[]"
        return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """ A method  that writes the JSON string
            representation of list_objs to a file
        Args:
            list_objs:  is a list of instances who inherits of Base
        """

        filename = "{}.json".format(cls.__name__)
        dict_list = []

        if not list_objs:
            pass
        else:
            for i in range(len(list_objs)):
                dict_list.append(list_objs[i].to_dictionary())

        json_list = cls.to_json_string(dict_list)

        with open(filename, "w") as f:
            f.write(json_list)

    @staticmethod
    def from_json_string(json_string):
        """ A method that returns the list of
            the JSON string representation json_string
        Args:
            json_string: json representation
        """

        if not json_string:
            return []
        return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """ A method that returns an instance with
            all attributes already set
        Args:
            dictionary: dictionary of attributes and their values
        """

        if cls.__name__ == "Rectangle":
            new = cls(2, 2)
        else:
            new = cls(2)
        new.update(**dictionary)
        return new

    @classmethod
    def load_from_file(cls):
        """ A method that returns a list of instances"""

        filename = "{}.json".format(cls.__name__)

        if os.path.exists(filename) is False:
            return []

        with open(filename, "r") as f:
            read_list = f.read()

        class_list = cls.from_json_string(read_list)
        instance_list = []

        for i in range(len(class_list)):
            instance_list.append(cls.create(**class_list[i]))

        return instance_list
