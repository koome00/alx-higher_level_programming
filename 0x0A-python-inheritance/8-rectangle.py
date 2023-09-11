#!/usr/bin/python3
"""
Module 8-base_geometry

Defines class BaseGeometry with
public instance methods

Defines a subclass Rectangle of class Base geometry
"""


class BaseGeometry():
    """
    Methods:
        area(self)
        integer_validator(self, name, value)
    """
    def area(self):
        """ raises an exception"""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """
        validates value
        Attributes:
            name(str) :will be a string
            value(int) : integer
        """
        if type(value) is not int:
            raise TypeError("{:s} must be an integer".format(name))
        elif value <= 0:
            raise ValueError("{:s} must be greater than 0".format(name))

class Rectangle(BaseGeometry):
    """
    defines class rectangle

    Methods:
        __init__(self, width, height)

    Attributes:
        width (int): width of rectangle
        height (int): height of rectangle
    """
    def __init__(self, width, height):
        """
        Initializer

        Attributes:
            width (int): rectangle width
            height (int): rectangle height
        """
        super().integer_validator("width", width)
        self.__width = width
        super().integer_validator("height", height)
        self.__height = height

