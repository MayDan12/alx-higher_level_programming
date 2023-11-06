#!/usr/bin/python3
"""This Defines a function that adds attributes to objects."""


def add_attribute(obj, att, value):
    """This function Add a new attribute to an object if possible.

    Args:
        obj (any): object to add an attribute to.
        att (str): name of the attribute to add to obj.
        value (any): value of att.
    Raises:
        TypeError: attribute cannot be added.
    """
    if not hasattr(obj, "__dict__"):
        raise TypeError("can't add new attribute")
    setattr(obj, att, value)
