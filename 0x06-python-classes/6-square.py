#!/usr/bin/python3
"""Defination of class 'Square' with privet instance attribute"""


class Square:
    """Class Square that defines a square.
    """
    def __init__(self, size=0, position=(0, 0)):
        """Inits Square with privet instance attribute 'size'

        Args:
            size: Size of the square with integer value
            position: A tuple for the position of the square

        Raises:
            TypeError: When size is not integer
            ValueError: When size is negative
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size
        self.__position = position

    def area(self):
        """Calculates the area of a square"""
        return self.__size * self.__size

    @property
    def size(self):
        """ Returns the size value"""
        return self.__size

    @size.setter
    def size(self, value):
        """Sets the size value of the square

        Args:
            value: Size of the square to be set with integer value

        Raises:
            TypeError: When size is not integer
            ValueError: When size is negative
        """
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value


    @property
    def position(self):
        """ Retrieves the position of the square

        Returns:
            position of the square
        """
        return self.__position

    @position.setter
    def position(self, value):
        """ Sets the position of the square

        Args:
            value: position value of the square

        Raises:
            TypeError: position is not tuple of 2 postive numbers
        """
        if not isinstance(value, tuple):
            raise TypeError("position must be a tuple of 2 positive integers")
        if len(value) != 2:
            raise TypeError("position must be a tuple of 2 positive integers")
        if not isinstance(value[0], int):
            raise TypeError("position must be a tuple of 2 positive integers")
        if not instance(value[1], int):
            raise TypeError("position must be a tuple of 2 positive integers")
        if value[0] < 0 or value[1] < 0:
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value

    def my_print(self):
        """ Prints the square with the # character"""
        if not self.__size:
            print()
        else:
            for i in range(self.__position[1]):
                print()
            for i in range(self.__size):
                for m in range(self.__position[0]):
                    print(" ", end='')
                for j in range(self.__size):
                    print("#", end='')
                print()
