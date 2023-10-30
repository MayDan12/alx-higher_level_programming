#!/usr/bin/python3
# 4-print_square.py
"""Defines a function that's prints a square"""

def print_square(size):
    """This function print a square with the # character.

    Args:
        size (int): The height/width of the square.
    Raises:
        TypeError: if size is not an integer.
        ValueError: if size is < 0 okay
    """
    if not isinstance(size, int):
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")

    for d in range(size):
        [print("#", end="") for f in range(size)]
        print("")
