#!/usr/bin/python3
"""A model that contains the Square class"""

Rectangle = __import__("9-rectangle").Rectangle


class Square(Rectangle):
    """The Square class"""
    def __init__(self, size):
        """Creates a new instance of Square
        Args:
        size (int): the side length of the square"""
        self.integer_validator("size", size)
        self.__size = size
        super().__init__(size, size)

    def __str__(self):
        return f"[Square] {self.__size}/{self.__size}"
