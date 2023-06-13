#!/usr/bin/python3
"""A module that contains a function to convert a class instance
into a json object"""


def class_to_json(obj):
    """converts ''obj'' into a json object
    Args:
        obj (object): the object instance to convert into a json object"""
    return obj.__dict__
