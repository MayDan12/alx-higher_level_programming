#!/usr/bin/python3
"""This Defines a Python class-to-JSON function."""


def class_to_json(obj):
    """This function Return the dictionary represntation of a simple data structure."""
    return obj.__dict__
