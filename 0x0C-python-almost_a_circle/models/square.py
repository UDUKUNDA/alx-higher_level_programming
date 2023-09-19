#!/usr/bin/python3
"""This the Module for Square class that inherits from Rectangle"""

from models.rectangle import Rectangle

class Square(Rectangle):
    """Square class inherits from Rectangle"""

    def __init__(self, size, x=0, y=0, id=None):
        """Initialize Square instance"""

        super().__init__(size, size, x, y, id)

        @property
    def size(self):
        """Here is the Getter for size attribute"""
        return self.width

    @size.setter
    def size(self, value):
        """and this is the Setter for size attribute"""

        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")

        self.width = value
        self.height = value


    def __str__(self):
        """Return string representation of the square"""

        return "[Square] ({}) {}/{} - {}".format(
            self.id, self.x, self.y, self.width)
    def update(self, *args, **kwargs):
        """Update square attributes based on arguments or keyword arguments"""

        if args:
            if len(args) >= 1:
                self.id = args[0]
            if len(args) >= 2:
                self.size = args[1]
            if len(args) >= 3:
                self.x = args[2]
            if len(args) >= 4:
                self.y = args[3]
        else:
            for key, value in kwargs.items():
                setattr(self, key, value)
    def to_dictionary(self):
        """Return dictionary representation of the square"""

        return {
            'id': self.id,
            'size': self.width,
            'x': self.x,
            'y': self.y
        }

