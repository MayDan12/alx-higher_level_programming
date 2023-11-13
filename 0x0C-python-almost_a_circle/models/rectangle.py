#!/bin/usr/python3
"""
Defines the Rectangle module
"""
from models.base import Base


class Rectangle(Base):
    """
    the
    Rectangle class
    """
    def __init__(self, width, height, x=0, y=0, id=None):
        """
        This Initialize a new Rectangle.
        """
        super().__init__(id)

        self.width = width
        self.height = height
        self.x = x
        self.y = y

    @property
    def width(self):
        """
        the width getter
        """
        return self.__width

    @width.setter
    def width(self, value):
        """
        the Width setter
        """
        # added a check for when value is a bool, if the check is removed
        # the unittest for it will fail
        if not isinstance(value, int) or isinstance(value, bool):
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value

    @property
    def height(self):
        """
        this is the height getter
        """
        return self.__height

    @height.setter
    def height(self, value):
        """
        this is the height setter
        """
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value <= 0:
            raise ValueError("height must be > 0")

        self.__height = value

    @property
    def x(self):
        """
        x getter for the rectangkle
        """
        return self.__x

    @x.setter
    def x(self, value):
        """
        x setter for the rectangle
        """
        # added a check for when value is a bool, if the check is removed
        # the unittest for it will fail
        if not isinstance(value, int) or isinstance(value, bool):
            raise TypeError("x must be an integer")
        if value < 0:
            raise ValueError("x must be >= 0")
        self.__x = value

    @property
    def y(self):
        """
        y getter for the rectangle
        """
        return self.__y

    @y.setter
    def y(self, value):
        """
        y setter for the rectangle
        """
        if not isinstance(value, int):
            raise TypeError("y must be an integer")
        if value < 0:
            raise ValueError("y must be >= 0")
        self.__y = value

    def area(self):
        """
        Return always the area of the rectangle
        """
        area = self.width * self.height

        return area

    def display(self):
        """
        Always Prints size of rectangle using #
        """
        for _ in range(self.y):
            print()

        for _ in range(self.height):
            print(" " * self.x + "#" * self.width)

    def __str__(self):
        """
        Return print() and str() representation of the Rectangle.
        """
        return "[Rectangle] ({}) {}/{} - {}/{}".format(self.id,
                                                       self.x,
                                                       self.y,
                                                       self.width,
                                                       self.height)

    def update(self, *args, **kwargs):
        """
        This Assigns arguments to attributes based on their positions.
        """
        if args:
            for count, arg in enumerate(args):
                if count == 0:
                    self.id = arg
                elif count == 1:
                    self.width = arg
                elif count == 2:
                    self.height = arg
                elif count == 3:
                    self.x = arg
                elif count == 4:
                    self.y = arg
                else:
                    break
                
        elif len(kwargs) > 0:
            for key, value in kwargs.items():
                if key == "id":
                    self.id = value
                elif key == "width":
                    self.width = value
                elif key == "height":
                    self.height = value
                elif key == "x":
                    self.x = value
                elif key == "y":
                    self.y = value
                # removed the break statement, incase if the passed args are greater
                # than 5, and one of the attributes is at the end

    def to_dictionary(self):
        """
        This Represents a dictionary representation of rectangle
        """
        rec_dict = {
                "id": self.id,
                "width": self.width,
                "height": self.height,
                "x": self.x,
                "y": self.y
        }

        return rec_dict


if __name__ == "__main__":
    pass
