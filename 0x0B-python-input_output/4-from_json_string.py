#!/usr/bin/python3
# 6-from_json_string.py
"""This Defines a JSON-to-object function."""
import json


def from_json_string(my_str):
    """This function Return the Python object representation of a JSON string."""
    return json.loads(my_str)
