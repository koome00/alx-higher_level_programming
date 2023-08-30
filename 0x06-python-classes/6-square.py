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
        position: position
    
    functons:
        __init__(self, size)
        area(self)
        size(self)
        size(self, value)
        position(self)
        position(self, value)
        my_print(self)
    """
    def __init__(self, size=0, position=(0, 0)):
        """
        intitializes square object

        Attribute:
            size: size of square sides
            position: position
        """
        self.size = size
        self.position = position

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

    @property
    def position(self):
        """
        Getter

        Return:
            position
        """
        return self.__position
    
    @position.setter
    def position(self, value):
        """
        Setter

        Attributes:
            value: position
        """

        if type(value) is not tuple or len(value) != 2 or \
           type(value[0]) is not int or type(value[1]) is not int or \
           value[0] < 0 or value[1] < 0:
            raise TypeError("position must be a tuple of 2 positive integers")
        else:
            self.__position = value



    def my_print(self):
        """
        Prints #
        """
        if self.__size == 0:
            print("")
        else:
            print("\n" * self.__position[1], end="")
            print("\n".join([" " * self.__position[0] +
                             "#" * self.__size
                             for rows in range(self.__size)]))



