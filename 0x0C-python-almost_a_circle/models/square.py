#!/usr/bin/python3
""" A module defining a class called Square inheriting a Rectangle class """


from models.rectangle import Rectangle


class Square(Rectangle):
    """ A class called Square inheriting the class Rectangle"""
    def __init__(self, size, x=0, y=0, id=None):
        """ A constructer method for the Square class
        Args:
            size: the size of a square instance
            x: the x component for square instance's coordinates
            y: the y component for square instance's coordinates
            id: the identification number for a Base instance
        """

        super().__init__(size, size, x, y, id)
        self.size = size

    def __str__(self):
        """ A formating method for the printing of a square instance"""
        string_1 = "[Square] "
        string_2 = "({}) ".format(self.id)
        string_3 = "{}/{} - ".format(self.x, self.y)
        string_4 = "{}".format(self.width)

        return string_1 + string_2 + string_3 + string_4

    @property
    def size(self):
        """ getter for size"""
        return self.width

    @size.setter
    def size(self, value):
        """ setter for size"""
        self.width = value
        self.height = value

    def update(self, *args, **kwargs):
        """ A method to update the values of instance attributes
        Args:
            *args: list of arguments
            **kwargs: dictinary of keys and values
        """
        if args is not None and len(args) != 0:
            attribute_list = ["id", "size", "x", "y"]
            for i in range(len(args)):
                if i == 1:
                    setattr(self, "width", args[i])
                    setattr(self, "heignt", args[i])
                else:
                    setattr(self, attribute_list[i], args[i])
        else:
            for key, value in kwargs.items():
                if key == "size":
                    setattr(self, "width", value)
                    setattr(self, "height", value)
                else:
                    setattr(self, key, value)

    def to_dictionary(self):
        """ A method returning a dictionary of attributes
        Returns:
            A dictionary of attributes
        """
        attribute_list = ["id", "size", "x", "y"]
        new_dict = {}

        for att in attribute_list:
            new_dict[att] = getattr(self, att)
        return new_dict
