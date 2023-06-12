#!/usr/bin/python3
"""model that contains function that detect if object is instance of a class"""


def is_same_class(obj, a_class):
    """checks if obj is instance of a_class"""
    if obj is None:
        return a_class is None
    if not hasattr(obj, '__class__') or not hasattr(a_class, "__name__"):
        return False
    return obj.__class__.__name__ == a_class.__name__
