#!/usr/bin/python3
"""
Module 3-square
Defines class square
"""

class Square():
    """
    class Square definition

    Args:
        size (int): size of a side in square
    """

    def __init__(self, size=0):
        """
        Will initialize square

        Atrributes:
            __size (int): size of square
        """
        if type(size) is not int:
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = size

    def area(self):
        """
        Finds area of square

        Returns: area
        """
        return self.__size ** 2
