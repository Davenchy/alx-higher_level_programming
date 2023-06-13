#!/usr/bin/python3
"""A model that contains a function to add a new attribute to an object"""


def add_attribute(obj, name, value):
    """sets attribute with ``name`` and ``value`` to ``obj`` only if possible
    """
    if not hasattr(obj, "__dict__") or not hasattr(obj, "__setattr__"):
        raise TypeError("can't add new attribute")
    obj.__setattr__(name, value)
