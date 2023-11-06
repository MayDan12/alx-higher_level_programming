#!/usr/bin/python3
"""This Defines a class MyInt that inherits from int."""


class MyInt(int):
    """This function Invert int operators == and !=."""

    def __eq__(self, value):
        """This Override == opeartor with != behavior."""
        return self.real != value

    def __ne__(self, value):
        """This Override != operator with == behavior."""
        return self.real == value
