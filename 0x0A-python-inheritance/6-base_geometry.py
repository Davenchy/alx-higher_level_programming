#!/usr/bin/python3
"""Model that contains an empty class"""


class BaseGeometry:
    """Geometry bass class"""
    def area(self):
        raise Exception("area() is not implemented")
