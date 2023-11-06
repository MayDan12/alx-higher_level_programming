#!/usr/bin/python3
"""This defines an inherited list class My list to uses"""

class MyList(list):
    """This function implements sorted printing for the built in class list."""
    def print_sorted(self):
        """This print a list in sorted ascending order"""
        print(sorted(self))
