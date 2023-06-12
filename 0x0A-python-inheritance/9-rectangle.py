#!/usr/bin/python3
"""A model that contains The Rectangle class"""

BaseGeometry = __import__("7-base_geometry").BaseGeometry


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

    def area(self):
        """Returns the area of the rectangle"""
        return self.__width * self.__height

    def __str__(self):
        return f"[Rectangle] {self.__width}/{self.__height}"
