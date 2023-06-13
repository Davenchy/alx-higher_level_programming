#!/usr/bin/python3
"""A module with the student class"""


class Student:
    """A Student class"""
    def __init__(self, first_name, last_name, age):
        """Initialize the student object
        Args:
            first_name (str): the student's first name
            last_name (str): the student's last name
            age (int): the student's age"""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        if type(attrs) is list and all(type(i) is str for i in attrs):
            return {a: getattr(self, a) for a in attrs if a in self.__dict__}
        return self.__dict__
