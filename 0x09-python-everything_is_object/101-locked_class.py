#!/usr/bin/python3
"""Module of a locked class"""


class LockedClass(object):
    """A locked class that only has first_name dynamic attribute"""
    def __setattr__(self, key, value):
        if key != "first_name":
            raise AttributeError(f"object has no attribute '{key}'")
        object.__setattr__(self, key, value)
