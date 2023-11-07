#!/usr/bin/python3
"""This reads a text file and print it out to the stdout"""

def read_file(filename=""):
    """This function reads a text file (UTF8) and prints it to stdout:"""

    try:
        with open(filename, 'r', encoding='utf-8') as file:
            for line in file:
                print ("{}".format(line), end='')
    except FileNotFoundError:
        print ("File '{}' not found.".format(filename))
    except Exception as e:
        print ("An error occurred: {}".format(e))
