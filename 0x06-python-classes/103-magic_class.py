#!/usr/bin/python3

"""Simple MagicClass that processes circle area and circumference"""

import math


class MagicClass:
    """Simple class that represents a circle object"""
    def __init__(self, radius=0):
        """Initialize circle magic class"""
        self.__radius = 0
        if type(radius) is not int and type(radius) is not float:
            raise TypeError("radius must be a number")
        self.__radius = radius

    def area(self):
        """returns the area of the circle"""
        return self.__radius ** 2 * math.pi

    def circumference(self):
        """returns the circumference of the circle"""
        return 2 * math.pi * self.__radius
