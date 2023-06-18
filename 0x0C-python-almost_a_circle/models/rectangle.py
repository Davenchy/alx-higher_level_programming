#!/usr/bin/python3
"""The Rectangle class that inherits from The Base class"""

from models.base import Base


class Rectangle(Base):
    """The Rectangle class"""

    def __init__(self, width, height, x=0, y=0, id=None):
        """Initialize the Rectangle class

        Args:
            width (int): the width of the rectangle
            height (int): the height of the rectangle
            x (int): the x-axis coordinate of the rectangle
            y (int): the y-axis coordinate of the rectangle
            id (int|None): the id of the rectangle"""
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    @property
    def width(self):
        """Get the width of the rectangle

        Returns:
            int: the width of the rectangle"""
        return self.__width

    @property
    def height(self):
        """Get the height of the rectangle

        Returns:
            int: the height of the rectangle"""
        return self.__height

    @property
    def x(self):
        """Get the x-axis coordinate of the rectangle

        Returns:
            int: the x-axis coordinate of the rectangle"""
        return self.__x

    @property
    def y(self):
        """Get the y-axis coordinate of the rectangle

        Returns:
            int: the y-axis coordinate of the rectangle"""
        return self.__y

    @width.setter
    def width(self, value):
        """Set the width value of the rectangle"""""
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value

    @height.setter
    def height(self, value):
        """Set the height value of the rectangle"""
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value <= 0:
            raise ValueError("height must be > 0")
        self.__height = value

    @x.setter
    def x(self, value):
        """Set the x-axis coordinate value of the rectangle"""
        if not isinstance(value, int):
            raise TypeError("x must be an integer")
        if value < 0:
            raise ValueError("x must be >= 0")
        self.__x = value

    @y.setter
    def y(self, value):
        """Set the y-axis coordinate value of the rectangle"""
        if not isinstance(value, int):
            raise TypeError("y must be an integer")
        if value < 0:
            raise ValueError("y must be >= 0")
        self.__y = value

    def area(self):
        """Calculate the area of the rectangle

        Returns:
            int: the area of the rectangle"""
        return self.width * self.height

    def display(self):
        """Display the rectangle on the screen"""
        if self.__y:
            print("\n" * self.__y, end='')
        print(((' ' * self.__x) + '#' * self.__width + '\n') * self.__height,
              end='')

    def __str__(self):
        return f"""[Rectangle] ({self.id}) {self.__x}/{self.__y} - {
        self.__width}/{self.__height}"""
