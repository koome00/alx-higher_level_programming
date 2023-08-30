#!/usr/bin/python3
"""
Module 5-square
Defines a square
"""

class Square:
    """
    class Square - defines a square

    Args":
        size: size of square sides

    Functions:
    """

    def __init__(self, size=0):
        """
        Initialize size

        Attributes:
            size: size of sides
        """

        self.size = size

    @property
    def size(self):
        '''
        Getter

        Returns: size
        '''
        return self.__size

    @size.setter
    def size(self, value):
        """
        Sets new size value

        Attributes:
            value: new size
        """

        if type(value) is not int:
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = value
    

    def area(self):
        """
        Calculatea area of square

        Returns:
            area
        """
        return (self.__size) ** 2

    

    def my_print(self):
        """
        Prints in stdout the square with the character #

        Attributes:
            s: #

        """
        s = "#"
        for i in range(self.__size):
            for j in range(self.__size):
                print("{}".format(s), end="")

            print("")
        








