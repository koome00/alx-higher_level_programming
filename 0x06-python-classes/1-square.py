#!/usr/bin/python3
"""
Module 1-square
Defines class Square with a private instance attribute
"""
class Square:
    """
    class to compute square

    Args:
        size (int): sides of a square
    """
    def __init__(self, size):
        """
        Initializes square instance
        
        Attributes:
            __size (int): size of square sides
        """
            
        self.__size = size
