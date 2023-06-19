#!/usr/bin/python3
"""Module of the base class"""

import json


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

    def to_dictionary(self):
        """converts instance into a dictionary of its attributes"""
        return self.__dict__

    @staticmethod
    def to_json_string(list_dictionaries):
        """Convert a list of dictionaries to a json string

        Args:
            list_dictionaries (list): the list of dictionaries to convert

        Returns:
            str: the json string"""
        if list_dictionaries is None:
            return "[]"
        if (not isinstance(list_dictionaries, list)
                or not all(isinstance(i, dict) for i in list_dictionaries)):
            raise TypeError("list_dictionaries must be a list of dicts")
        return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """Writes a list of objects that inherits from the Base class to a file
        of the same name of the class name"""
        objs = list_objs[:]
        for i in range(len(objs)):
            item = objs[i]
            if isinstance(item, Base):
                objs[i] = item.to_dictionary()
            else:
                raise TypeError(r"""list_objs items must be instances of
                    classes inherits from Base""")
        with open(cls.__name__ + ".json", "w") as file:
            file.write(cls.to_json_string(objs))
