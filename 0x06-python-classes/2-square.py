#!/usr/bin/python3

"""A nother fucking day, Who cares!?"""


class Square:
    """Simple Square Class, OMG!!"""

    def __init__(self, size=0) -> None:
        """The same fucking shit like the last task but this time size arg is
        optional and is type checked (be carful I will fuck you in your dreans)

        Args:
            size (int): The same fucking shit, (Squares has size, OMG!!)"""
        if type(size) is not int:
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size
