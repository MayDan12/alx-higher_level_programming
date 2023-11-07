#!/usr/bin/python3
"""Defines a function that write a string to a test file."""

def write_file(filename="", text=""):
    try:
        with open(filename, 'w', encoding='utf-8') as file:
            chars_written = file.write(text)
            return chars_written
    except Exception as e:
        print("An error occurred: {}".format(e))
        return 0
