#!/usr/bin/python3
""" A module that defines a class called Rectangle"""


from models.base import Base


class Rectangle(Base):
    """ A class defination for Rectangle"""

    def __init__(self, width, height, x=0, y=0, id=None):
        """ A constructer method for instances of Rectangle
        Args:
            width: the width of a rectangle instance
            height: the height of a rectangle instance
            x: the x component of a rectangle instance's coordinate
            y: the y component of a rectangle instance's coordinate
            id: the identification number of a Base instance
        """

        self.width = width
        self.height = height
        self.x = x
        self.y = y
        super().__init__(id)

    @property
    def width(self):
        """ getter for width"""
        return self.__width

    @width.setter
    def width(self, value):
        """ setter for width
        Raises:
            TypeError: if value is not integer
            ValueError: if value is less than or equal to 0
        """

        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value

    @property
    def height(self):
        """ getter for height"""
        return self.__height

    @height.setter
    def height(self, value):
        """ setter for height
         Raises:
            TypeError: if value is not integer
            ValueError: if value is less than or equal to 0
        """
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value <= 0:
            raise ValueError("height must be > 0")
        self.__height = value

    @property
    def x(self):
        """ getter for x"""
        return self.__x

    @x.setter
    def x(self, value):
        """ setter for x
        Raises:
            TypeError: if value is not an integer
            ValueError: if value is less than 0
        """
        if not isinstance(value, int):
            raise TypeError("x must be an integer")
        if value < 0:
            raise ValueError("x must be >= 0")
        self.__x = value

    @property
    def y(self):
        """ getter for y"""
        return self.__y

    @y.setter
    def y(self, value):
        """ setter for y
        Raises:
            TypeError: if value is not an integer
            ValueError: if value is less than 0
        """
        if not isinstance(value, int):
            raise TypeError("y must be an integer")
        if value < 0:
            raise ValueError("y must be >= 0")
        self.__y = value

    def area(self):
        """ A method that calculates the area of a rectangle instance"""
        return self.__width * self.__height

    def display(self):
        """ A method to display a rectangle instances using the # character"""
        print("\n" * self.y, end="")
        for i in range(self.__height):
            print(" " * self.x, end="")
            print("#" * self.__width)

    def __str__(self):
        """ Formats how a rectangle instance is going to be printed"""
        string_1 = "[Rectangle] "
        string_2 = "({}) ".format(self.id)
        string_3 = "{}/{} - ".format(self.x, self.y)
        string_4 = "{}/{}".format(self.width, self.height)

        return string_1 + string_2 + string_3 + string_4

    def update(self, *args, **kwargs):
        """ A method to update the values of instance attributes
        Args:
            *args: list of arguments
        """

        if args is not None and len(args) != 0:
            attribute_list = ["id", "width", "height", "x", "y"]
            for i in range(len(args)):
                setattr(self, attribute_list[i], args[i])
        else:
            for key, value in kwargs.items():
                setattr(self, key, value)

    def to_dictionary(self):
        """ A method returning a dictionary of attributes
        Returns:
            A dictionary of attributes
        """
        attribute_list = ["id", "width", "height", "x", "y"]
        new_dict = {}

        for att in attribute_list:
            new_dict[att] = getattr(self, att)
        return new_dict
