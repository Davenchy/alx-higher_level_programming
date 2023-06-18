#!/usr/bin/python3
"""Module of the base class"""


class Base:
    """The Base Class"""
    __nb_objects = 0

    def __init__(self, id=None):
        """Initialize a new instance of the base class with an id
        if ''id'' was set then its value is applied as ''id'' attr otherwise
        a auto increment id value will be set

        Args:
            id (int|None): the id of the current instance"""
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
