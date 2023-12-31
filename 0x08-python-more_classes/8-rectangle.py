#!/usr/bin/python3
"""
Module 1-rectangle
Defines a rectangle and takes private attributes
width and height
"""


class Rectangle():
    """
    class Rectangle definition

    Args:
        width (int): rectangle width
        height (int): height of rectangle
        value (int): value to set
        number_of_instances (int): number of instances
        print_symbol : pound symbol

    Functions:
        __init__(self, width = 0, height = 0)
        width(self)
        width(self, value)
        height(self, value)
        height(self)
        area(self)
        perimeter(self)
        __str__(self)
        __repr__(self)
        __del__(self)
        bigger_or_equal(rect_1, rect_2)
    """

    number_of_instances = 0
    print_symbol = "#"

    def __init__(self, width=0, height=0):
        """
        Initializer

        Attributes:
            width: rectangle width
        """
        self.width = width
        self.height = height
        Rectangle.number_of_instances += 1

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
            raise TypeError("width must be an integer")
        elif value < 0:
            raise ValueError("width must be >= 0")
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
            raise TypeError("width must be an integer")
        elif value < 0:
            raise ValueError("width must be >= 0")
        else:
            self.__height = value

    def area(self):
        """ Returns area of rectangle"""
        return self.__width * self.__height

    def perimeter(self):
        """Returns perimeter of rectangle"""
        if self.__width == 0 or self.__height == 0:
            return 0
        else:
            return (self.__width * 2) + (self.__height * 2)

    def __str__(self):
        """ string magic method """
        result = ""
        if self.__width == 0 or self.__height == 0:
            return result
        else:
            pic = "\n".join([str(Rectangle.print_symbol) *
                self.__width for rows in range(self.__height)])
        return pic

    def __repr__(self):
        """ __repr__ magic method"""
        return ("Rectangle" + "(" + str(self.__width)
                + ", " + str(self.__height) + ")")

    def __del__(self):
        """ Deletes instance"""
        print("Bye rectangle...")
        Rectangle.number_of_instances -= 1

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        if not isinstance(rect_1, Rectangle):
            raise TypeError("rect_1 must be an instance of Rectangle")
        if not isinstance(rect_2, Rectangle):
            raise TypeError("rect_2 must be an instance of Rectangle")
        if rect_1.area() >= rect_2.area():
            return rect_1
        return rect_2
