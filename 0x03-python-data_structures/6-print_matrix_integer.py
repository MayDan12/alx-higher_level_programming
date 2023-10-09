#!/usr/bin/python3
# 6-print_matrix_integer.py

def print_matrix_integer(matrix=[[]]):
    """This function is very good."""
    for rows in matrix:
        for column in rows:
            print("{:d}".format(column), end="" if column != rows[-1] else "")
        print()
