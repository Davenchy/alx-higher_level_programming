#!/usr/bin/python3

"""module that contains MyList class which inherits from list type"""


class MyList(list):
    """My custom list type"""

    def print_sorted(self):
        """sort the list in ascending order the print"""
        print(sorted(self))
