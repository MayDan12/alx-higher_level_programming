#!/usr/bin/python3
"""This Defines a JSON file-reading function."""
import json


def load_from_json_file(filename):
    """This function Create a Python object from a JSON file."""
    with open(filename) as h:
        return json.load(h)
