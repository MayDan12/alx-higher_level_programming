#!/usr/bin/python3
"""Define a class Square."""


class Square:
    """ This is a function Represent a square."""

    def __init__(self, size=0):
        """THis function Initialize a new square.
        Args:
            size (int): this is The size of the new square.
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

    def area(self):
        """Return to the current area of the square."""
        return (self.__size * self.__size)
