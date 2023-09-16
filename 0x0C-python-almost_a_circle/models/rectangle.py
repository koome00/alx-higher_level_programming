#!/usr/bin/python3
"""
Module rectangle

Defines a class rectangle that inherits from
Base class
"""


from models.base import Base


class Rectangle(Base):
    """
    defines a class Rectangle

    Class attributes:
        __width (int): width of ractangle
        __height (int): heigth of rectangle
        __x (int): x
        __y (int): y

    Inherited attributes:
        id (int): private attribute of Base

    Methods:
        __init__
        update(self, *args, **kwargs)
        width(self)      width(self, value)
        height(self)     height(self, value)
        x(self)          x(self, value)
        y(self)          y(self, value)
        area(self)       display(self)
        __str__          to_dictionary(self)
    """

    def __init__(self, width, height, x=0, y=0, id=None):
        """rectangle constructor"""
        self.width = width
        self.height = height
        self.x = x
        self.y = y
        Base.__init__(self, id)

    @property
    def width(self):
        """width getter"""
        return self.__width

    @width.setter
    def width(self, value):
        """width setter"""
        if type(value) is not int:
            raise TypeError("width is not an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        else:
            self.__width = value

    @property
    def height(self):
        """height getter"""
        return self.__height

    @height.setter
    def height(self, value):
        """height setter"""
        if type(value) is not int:
            raise TypeError("height is not an integer")
        if value <= 0:
            raise ValueError("height must be > 0")
        else:
            self.__height = value

    @property
    def x(self):
        """getter function"""
        return self.__x

    @x.setter
    def x(self, value):
        """setter function"""
        if type(value) is not int:
            raise TypeError("x is not an integer")
        if value < 0:
            raise ValueError("x must be > 0")
        else:
            self.__x = value

    @property
    def y(self):
        """getter function"""
        return self.__y

    @y.setter
    def y(self, value):
        """setter function"""
        if type(value) is not int:
            raise TypeError("y is not an integer")
        if value < 0:
            raise ValueError("y must be > 0")
        else:
            self.__y = value

    def area(self):
        """method for calculating area"""
        return self.__width * self.__height

    def display(self):
        """prints in stdout rectangle instance with #"""
        if self.__y > 0:
            print("\n" * self.__y)
            for i in range(self.__height):
                print(" " * self.__x, end="")
                print("#" * self.__width)
        else:
            for i in range(self.__height):
                print(" " * self.__x, end="")
                print("#" * self.__width)

    def __str__(self):
        """str descriptor"""
        return ("[{:s}] ({:d}) {:d}/{:d} - {:d}/{:d}".format(
            self.__class__.__name__, self.id, self.__x, self.__y,
            self.__width, self.__height))

    def update(self, *args, **kwargs):
        """
        If args: set attributes in this order: id, width, height, x, y
        If no args given: set attributes according to kwargs
        """
        if args:
            for k, v in enumerate(args):
                if k == 0:
                    self.id = v
                elif k == 1:
                    self.width = v
                elif k == 2:
                    self.height = v
                elif k == 3:
                    self.x = v
                else:
                    self.y = v
        else:
            if "id" in kwargs:
                self.id = kwargs["id"]
            if "width" in kwargs:
                self.width = kwargs["width"]
            if "height" in kwargs:
                self.height = kwargs["height"]
            if "x" in kwargs:
                self.x = kwargs["x"]
            if "y" in kwargs:
                self.y = kwargs["y"]

    def to_dictionary(self):
        """Return dictionary representation"""
        d = {}
        d["id"] = self.id
        d["width"] = self.width
        d["height"] = self.height
        d["x"] = self.x
        d["y"] = self.y
        return d
