#!/usr/bin/python3
"""A model of the class Square which inherits from the Rectangle class"""
from models.rectangle import Rectangle


class Square(Rectangle):
    """The Square class based on the Rectangle class"""

    def __init__(self, size, x=0, y=0, id=None):
        """Initialize the instance of the Square class

        Args:
            size (int): the size of the square
            x (int): the x-axis coordinate value of the square
            y (int): the y-axis coordinate value of the square
            id (int|None): the id of the current square"""
        super().__init__(size, size, x, y, id)

    @property
    def size(self):
        """Returns the size of the side length of the square"""
        return self.width

    @size.setter
    def size(self, value):
        """Sets the value if the square's side length"""
        self.width = value
        self.height = value

    def __str__(self):
        return f"[Square] ({self.id}) {self.x}/{self.y} - {self.width}"
