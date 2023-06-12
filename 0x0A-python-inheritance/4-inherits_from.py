#!/usr/bin/python3
"""A module that contains a function that detect direct/indirect inheritance to
a class"""


def inherits_from(obj, a_class):
    """Returns True if ''obj'' inherits from a class that directly/indirectly
    inherits from ''a_class''"""
    if not hasattr(obj, "__class__"):
        return False
    try:
        return (issubclass(obj.__class__, a_class) and
                obj.__class__ is not a_class)
    except Exception:
        return False
