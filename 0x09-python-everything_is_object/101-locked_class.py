#!/usr/bin/python3
"""Module of a locked class"""


class LockedClass(object):
    """A locked class that only has first_name dynamic attribute"""
    __slots__ = ['first_name']
