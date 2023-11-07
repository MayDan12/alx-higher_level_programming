#!/usr/bin/python3
"""This Defines a text file insertion function."""


def append_after(filename="", search_string="", new_string=""):
    """This function Insert text after each line containing a given string in a file.

    Args:
        filename (str): name of the file.
        search_string (str): string to search for within the file.
        new_string (str): string to insert.
    """
    texts = ""
    with open(filename) as r:
        for line in r:
            texts += line
            if search_string in line:
                texts += new_string
    with open(filename, "w") as w:
        w.write(texts)
