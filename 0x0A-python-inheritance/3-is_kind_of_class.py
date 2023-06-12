#!/usr/bin/python3
"""A module that contians a function that returns True if class is a super of
object"""


def is_kind_of_class(obj, a_class):
    """Returns True if ''obj'' is an instance of ''a_class'' or ''a_class''
    is a super class of ''obj''"""
    isin = isinstance(obj, a_class)
    if not isin:
        try:
            isin = issubclass(obj, a_class)
        except Exception:
            pass
    return isin
