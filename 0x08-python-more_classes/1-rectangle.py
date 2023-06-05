#!/usr/bin/python3

"""Define the Rectangle class at this module"""


class Rectangle:
    """A rectangle class"""

    def __init__(self, width=0, height=0):
        """Create new instance of the Rectangle class

        Args:
            width (int): the width of the rectangle
            height (int): the height of the rectangle"""
        self.width = width
        self.height = height

    @property
    def width(self):
        """The width of the rectangle"""
        return self.__width

    @width.setter
    def width(self, width):
        if type(width) is not int:
            raise TypeError("width must be an integer")
        elif width < 0:
            raise ValueError("width must be >= 0")
        self.__width = width

    @property
    def height(self):
        """The height of the rectangle"""
        return self.__height

    @height.setter
    def height(self, height):
        if type(height) is not int:
            raise TypeError("height must be an integer")
        elif height < 0:
            raise ValueError("height must be >= 0")
        self.__height = height
