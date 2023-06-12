#!/usr/bin/python3
"""A model that contains BaseGeometry class and subclasses"""


class BaseGeometry:
    """Geometry bass class"""
    def area(self):
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """Validate that value is integer and greater than 0"""
        if type(value) is not int:
            raise TypeError(f"{name} must be an integer")
        if value <= 0:
            raise ValueError(f"{name} must be greater than 0")


class Rectangle(BaseGeometry):
    """A Rectangle class based on the BaseGeometry class"""
    def __init__(self, width, height):
        """Creates an instance of Rectangle class
        Args:
            width (int): the rectangle width
            height (int): the rectangle height"""
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height
