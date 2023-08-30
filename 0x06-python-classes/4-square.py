#!/usr/bin/python3
"""
Module 4-square
Defines class square
"""

class Square:
    """
    Class square definition

    args:
        size: size of square
    
    functons:
        __init__(self, size)
        area(self)
    """
    def __init__(self, size=0):
        """
        intitializes square object

        Attribute:
            size: size of square sides
        """
        self.size = size

    def area(self):
        """
        Calculatea area of square

        Returns:
            area
        """
        return (self.__size) ** 2

    @property
    def size(self):
        """
        Gets size

        Returns:
            size
        """

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










