#!/usr/bin/python3
"""
Module 7-base_geometry

Defines class BaseGeometry with
public instance methods
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
