#!/usr/bin/python3
"""
Module 2-is_same_class

Checks object instance
"""


def is_same_class(obj, a_class):
    """
    Returns:
        True if the object is exactly an
        instance of the specified class ; otherwise Fals
    """
    return type(obj) == a_class
