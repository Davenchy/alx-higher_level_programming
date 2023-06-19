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

    def update(self, *args, **kwargs):
        """Updates the square attributes using positional arguments or
        keyworded arguments, can not use both at the same time.

        The order of the positional arguments:
            #0: id
            #1: size
            #2: x
            #3: y"""
        args = list(args)
        if len(args) >= 2:
            args = args[:2] + args[1:]
        if 'width' in kwargs:
            del kwargs['width']
        if 'height' in kwargs:
            del kwargs['height']
        if 'size' in kwargs:
            kwargs['width'] = kwargs['size']
            kwargs['height'] = kwargs['size']
        super().update(*args, **kwargs)

    def to_dictionary(self):
        """Returns a dictionary with all attributes of the square

        Attributes:
            id, x, y, size"""
        data = super().to_dictionary()
        data['size'] = data['width']
        del data['width']
        del data['height']
        return data

    def __str__(self):
        return f"[Square] ({self.id}) {self.x}/{self.y} - {self.width}"
