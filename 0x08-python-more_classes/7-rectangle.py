#!/usr/bin/python3

"""Define the Rectangle class at this module"""


class Rectangle:
    """A rectangle class"""
    number_of_instances = 0
    print_symbol = '#'

    def __init__(self, width=0, height=0):
        """Create new instance of the Rectangle class

        Args:
            width (int): the width of the rectangle
            height (int): the height of the rectangle"""
        self.width = width
        self.height = height
        Rectangle.number_of_instances += 1

    @property
    def width(self):
        """The width of the rectangle"""
        return self.__width

    @width.setter
    def width(self, width):
        if type(width) is not int:
            raise TypeError("width must be an integer")
        elif width < 0:
            raise ValueError("width must be >= 0")
        self.__width = width

    @property
    def height(self):
        """The height of the rectangle"""
        return self.__height

    @height.setter
    def height(self, height):
        if type(height) is not int:
            raise TypeError("height must be an integer")
        elif height < 0:
            raise ValueError("height must be >= 0")
        self.__height = height

    def area(self):
        """Returns the area of  the rectangle

        Example:
            >>> Rectangle(2, 3).area() # 2 * 3
            6"""
        return self.__width * self.__height

    def perimeter(self):
        """Returns the perimeter of the rectangle only if width and height != 0

        Example:
            >>> Rectangle(2, 3).perimeter() # 2 * (2 + 3)
            10

            >>> Rectangle(0, 1).perimeter()
            0"""
        if self.__width == 0 or self.__height == 0:
            return 0
        return 2 * (self.__width + self.__height)

    def __str__(self):
        return "" if self.perimeter() == 0 else "\n".join(
            ["".join([Rectangle.print_symbol for _ in range(self.__width)])
                for _ in range(self.__height)])

    def __repr__(self):
        return f"Rectangle({self.__width}, {self.__height})"

    def __del__(self):
        Rectangle.number_of_instances -= 1
        print("Bye rectangle...")
