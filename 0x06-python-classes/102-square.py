#!/usr/bin/python3

"""A magic square class that do nothing usefull"""


class Square:
    """Simple Square Class, OMG!!"""

    def __init__(self, size=0) -> None:
        """Initialize the square class

        Args:
            size (int): The size of the square
            position (tuple): the position of the square"""
        self.size = size

    @property
    def size(self):
        """returns the value of the size attr"""
        return self.__size

    @size.setter
    def size(self, size):
        """Assign value for the private size attribute"""
        if type(size) is not int:
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

    def area(self):
        """Calculate the area value of the square"""
        return self.__size ** 2

    def __lt__(self, other):
        if not isinstance(other, Square):
            raise TypeError("other must be a Square object")
        return self.area() < other.area()

    def __gt__(self, other):
        if not isinstance(other, Square):
            raise TypeError("other must be a Square object")
        return self.area() > other.area()

    def __le__(self, other):
        if not isinstance(other, Square):
            raise TypeError("other must be a Square object")
        return self.area() <= other.area()

    def __ge__(self, other):
        if not isinstance(other, Square):
            raise TypeError("other must be a Square object")
        return self.area() >= other.area()

    def __eq__(self, other):
        if not isinstance(other, Square):
            raise TypeError("other must be a Square object")
        return self.area() == other.area()

    def __ne__(self, other):
        if not isinstance(other, Square):
            raise TypeError("other must be a Square object")
        return self.area() != other.area()
