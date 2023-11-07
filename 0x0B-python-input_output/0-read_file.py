#!/usr/bin/python3
"""This reads a text file and print it out to the stdout"""

def read_file(filename=""):
    """This function reads a text file (UTF8) and prints it to stdout:"""
    with open(filename, encoding="utf-8") as f:
        print(f.read(), end="")
