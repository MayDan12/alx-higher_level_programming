#!/usr/bin/python3
"""This Defines an inherited list class MyList."""

class MyList(list):
    """This function Implements sorted printing for the built-in list class."""

    def print_sorted(self):
        """This Print a list in sorted ascending order."""
        print(sorted(self))
