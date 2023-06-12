#!/usr/bin/python3
"""Model that contains an empty class"""


class BaseGeometry:
    """Geometry bass class"""
    def area(self):
        """Returns the area of the geometry"""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """Validate that value is integer and greater than 0"""
        if type(value) is not int:
            raise TypeError(f"{name} must be an integer")
        if value <= 0:
            raise ValueError(f"{name} must be greater than 0")
