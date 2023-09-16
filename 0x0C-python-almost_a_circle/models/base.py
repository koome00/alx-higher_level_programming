#!/usr/bin/python3
"""
Module Base

Contains Class base
Will be the base class for all other classes
in the this project
"""


class Base():
    """
    Defines class Base

    Class attributes:
        __nb_objects (int): number of objects

    Methods:
        __init__(self, id=None)
    """

    __nb_objects = 0

    def __init__(self, id=None):
        """class initializer"""
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
