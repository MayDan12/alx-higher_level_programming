#!/usr/bin/python3
"""This class Define a class Square."""
class Square:
    """This module Represent a squares."""

    def __init__(self, size=0):
        """This function Initialize a new square.
        Args:
            size (int): This is  The size of the new squares.
        """
        self.size = size

    @property
    def size(self):
        """Get/set the current size square."""
        return (self.__size)

    @size.setter
    def size(self, value):
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """Return the current square."""
        return (self.__size * self.__size)
