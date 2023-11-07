#!/usr/bin/python3
"""This Defines a file-appending function."""


def append_write(filename="", text=""):
    """This function Appends a string to the end of a UTF8 text file.

    Args:
        filename (str): name of the file to append to.
        text (str): string to append to the file.
    Returns:
        number of characters appended.
    """
    with open(filename, "a", encoding="utf-8") as f:
        return f.write(text)
