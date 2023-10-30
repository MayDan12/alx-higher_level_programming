#!/usr/bin/python3
# 3-rectangle.py

"""Defines The Rectangle class."""


class Rectangle:
    """This Represent a rectangle."""

    def __init__(self, width=0, height=0):
        """This Initialize a new Rectangle.

        Args:
            width (int): width of the new rectangle.
            height (int): height of the new rectangle.
        """
        self.width = width
        self.height = height

    @property
    def width(self):
        """The Get/set the width of the Rectangle."""
        return self.__width

    @width.setter
    def width(self, value):
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """The Get/set the height of the Rectangle."""
        return self.__height

    @height.setter
    def height(self, value):
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """This Return the area of the Rectangle."""
        return (self.__width * self.__height)

    def perimeter(self):
        """This Return the perimeter of the Rectangle."""
        if self.__width == 0 or self.__height == 0:
            return (0)
        return ((self.__width * 2) + (self.__height * 2))

    def __str__(self):
        """This Return the printable representation of the Rectangle.

        Represents the rectangle with the # character.
        """
        if self.__width == 0 or self.__height == 0:
            return ("")

        rects = []
        for d in range(self.__height):
            [rects.append('#') for j in range(self.__width)]
            if d != self.__height - 1:
                rects.append("\n")
        return ("".join(rects))
