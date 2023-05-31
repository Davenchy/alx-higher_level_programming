#!/usr/bin/python3

"""A nother fucking day, Who cares!?"""


class Square:
    """Simple Square Class, OMG!!"""

    def __init__(self, size=0, position=(0, 0)) -> None:
        """The same fucking shit like the last task but this time size arg is
        optional and is type checked (be carful I will fuck you in your dreans)

        Args:
            size (int): The same fucking shit, (Squares has size, OMG!!)
            position (tuple): the position of the square"""
        self.size = size
        self.position = position

    @property
    def size(self):
        """returns the value of the size attr"""
        return self.__size

    @size.setter
    def size(self, size):
        """Assign value for the private size attribute"""
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

    @property
    def position(self):
        """returns the position attr value"""
        return self.__position

    @position.setter
    def position(self, position):
        """Assign position value"""
        if (not isinstance(position, tuple) or len(position) != 2
                or not all(isinstance(v, int) and v >= 0 for v in position)):
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = position

    def area(self):
        """Calculate the fucking area value for the fucking square"""
        return self.__size ** 2

    def my_print(self):
        """prints the square using the '#' character to the stdout
        and whitespaces before the square accourding to the position attr"""
        if self.__size > 0:
            [print() for _ in range(self.__position[1])]
            for _ in range(self.__size):
                for _ in range(self.__position[0]):
                    print(" ", end="")
                for _ in range(self.__size):
                    print("#", end="")
                print()
        else:
            print()
