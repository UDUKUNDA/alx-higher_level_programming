#!/usr/bin/python3
"""This is for rectangle"""

from models.Base import Base

class Rectangle(Base):
    """This is the rectangle class that inherits from the BASE"""
        def __init__(self, width, height, x = 0, y = 0, id = None):
            """The constructor to initialise the instances of the
            Rectangle
            Parameters:
            wdth: this will be the width of a rectangle as integer
            height: Now this is going to be the height of the rectsngle in integers
            x: The x cordinate of the rectangle
            y: The y cordinate of the rectangle
            id:  The identinty of the rectangle

            Raises:
            TypeError: If one of the param height,  width, x, y is not an integer
            valueError: if either width or height or x, y is less than zero
            """
            super().__init__(id)
            
            self.width = width
            self.height = height
            self.x = x
            self.y = y
            
        @property
        def width(self)
        """Get/Set the width of the rectangle"""
        return self.__width

        @width.setter
        def width(self, value):
            """set the width of the rectangle"""
            if not isinstance(value, int):
                raise TypeError("The width must be an integer")
            if value <= 0:
                raise ValueError("width must be greater than zero")

            self.__width = value


         property
         def height(self):
         """Get height of the rectangle"""
         return self.__height

         @height.setter
         def height(self, value):
         """Set height of the rectangle"""
           if not isinstance(value, int):
               raise TypeError("height must be an integer")
           if value <= 0:
               raise ValueError("height must be > 0")

           self.__height = value

        @property
        def x(self):
        """Get x-coordinate of the rectangle"""
        return self.__x

        @x.setter
        def x(self, value):
        """Set x-coordinate of the rectangle"""

            if not isinstance(value, int):
                raise TypeError("x must be an integer")
            if value < 0:
                raise ValueError("x must be >= 0")

        self.__x = value

        @property
        def y(self):
        """Get y-coordinate of the rectangle"""
        return self.__y

        @y.setter
        def y(self, value):
        """Set y-coordinate of the rectangle"""

            if not isinstance(value, int):
                raise TypeError("y must be an integer")
            if value < 0:
                raise ValueError("y must be >= 0")
            self.__y = value
        def area(self<):
            """This wil claculate and return the area of a rectangle"""
            return self.__width * self.__height
        def dispaly(self):
            """The method will display the rectangle using '#' """
            for i in range(self.__height):
                print("#" * self.__width)

        def __str__(self):
        """The following will be the  string representation of the rectangle"""

        return "[Rectangle] ({}) {}/{} - {}/{}".format(
            self.id, self.__x, self.__y, self.__width, self.__height)

        def display(self):
        """Display the rectangle by handling the proper x and y offsets"""

            for _ in range(self.__y):
                print()
            for _ in range(self.__height):
                print(" " * self.__x + "#" * self.__width)
        def update(self, *args):
        """An Update of the rectangle attributes based on arguments"""

            if args:
                if len(args) >= 1:
                    self.id = args[0]
                if len(args) >= 2:
                    self.width = args[1]
                if len(args) >= 3:
                    self.height = args[2]
                if len(args) >= 4:
                    self.x = args[3]
                if len(args) >= 5:
                    self.y = args[4]
        def update(self, *args, **kwargs):
        """Update the rectangle attributes based on arguments or keyword arguments"""

            if args:
            """ If *args exists and is not empty, use it to update attributes"""
                if len(args) >= 1:
                    self.id = args[0]
                if len(args) >= 2:
                    self.width = args[1]
                if len(args) >= 3:
                    self.height = args[2]
                if len(args) >= 4:
                    self.x = args[3]
                if len(args) >= 5:
                    self.y = args[4]
            else:
                for key, value in kwargs.items():
                    setattr(self, key, value)
        def to_dictionary(self):
        """Return dictionary representation of the rectangle"""

        return {
            'id': self.id,
            'width': self.__width,
            'height': self.__height,
            'x': self.__x,
            'y': self.__y
        }

