#!/usr/bin/python3
"""
Module 1-rectangle
Defines a rectangle
"""


class Rectangle():
    """
    class Rectangle definition

    Args:
        width (int): rectangle width
        height (int): height of rectangle
        value (int): value to set

    Functions:
        __init__(self, width = 0, height = 0)
        width(self)
        width(self, value)
        height(self, value)
        height(self)
    """

    def __init__(self, width=0, height=0):
        """
        Initializer

        Attributes:
            width: rectangle width
        """
        self.width = width
        self.height = height

    @property
    def width(self):
        """
        Getter

        Return:
            returns width
        """

        return self.__width

    @width.setter
    def width(self, value):
        """
        Setter

        Attributes:
            value: value to set width
        """
        if type(value) is not int:
            return TypeError("width must be an integer")
        elif value < 0:
            return ValueError("width must be >= 0")
        else:
            self.__width = value

    @property
    def height(self):
        """
        Getter

        Return:
            returns height
        """

        return self.__height

    @height.setter
    def height(self, value):
        """
        Setter

        Attributes:
            value: value to set height
        """

        if type(value) is not int:
            return TypeError("width must be an integer")
        elif value < 0:
            return ValueError("width must be >= 0")
        else:
            self.__height = value
