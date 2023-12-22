#!/usr/bin/python3
""" Defination of class square """


class Square():
    """ class Square"""

    def __init__(self, size=0, position=(0, 0)):
        """ constractor method"""

        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        if not isinstance(position, tuple):
            raise TypeError("position must be a tuple of 2 positive integers")
        if len(position) != 2:
            raise TypeError("position must be a tuple of 2 positive integers")
        if not isinstance(position[0], int):
            raise TypeError("position must be a tuple of 2 positive integers")
        if not isinstance(position[1], int):
            raise TypeError("position must be a tuple of 2 positive integers")
        if position[0] < 0 or position[1] < 0:
            raise TypeError("position must be a tuple of 2 positive integers")

        self.__size = size
        self.__position = position

    def area(self):
        """ public instance method to calculate the area"""

        return (self.__size * self.__size)

    @property
    def size(self):
        """ getter for size"""

        return (self.__size)

    @size.setter
    def size(self, value):
        """setter for size"""

        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")

        self.__size = value

    @property
    def position(self):
        """getter for position"""

        return (self.__position)

    @position.setter
    def position(self, value):
        """setter for position"""

        if not isinstance(value, tuple):
            raise TypeError("position must be a tuple of 2 positive integers")
        if len(value) != 2:
            raise TypeError("position must be a tuple of 2 positive integers")
        if not isinstance(value[0], int) or not isinstance(value[1], int):
            raise TypeError("position must be a tuple of 2 positive integers")
        if value[0] < 0 or value[1] > 0:
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value

    def my_print(self):
        """ private instance method to print the square"""

        if not self.__size:
            print()
        else:
            print('\n' * self.__position[1], end='')
            for i in range(self.__size):
                print(' ' * self.__position[0], end='')
                print('#' * self.__size)

    def __str__(self):
        """formating method for printing"""

        printable = ""

        if not self.__size:
            return (printable)
        else:
            printable += ('\n' * self.__position[1])
            for i in range(self.__size):
                printable += (' ' * self.__position[0])
                printable += ('#' * self.__size)
                if i != self.__size - 1:
                    printable += ('\n')

        return (printable)
