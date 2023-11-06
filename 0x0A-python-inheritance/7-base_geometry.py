#!/usr/bin/python3
"""This Defines a base geometry class BaseGeometry."""


class BaseGeometry:
    """This function Reprsent base geometry."""

    def area(self):
        """This is Not yet implemented."""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """This function Validate a parameter as an integer.

        Args:
            name (str): name of the parameter.
            value (int): parameter to validate.
        Raises:
            ValueError: If value is <= 0.
            TypeError: If value is not an integer.
        """
        if type(value) != int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
