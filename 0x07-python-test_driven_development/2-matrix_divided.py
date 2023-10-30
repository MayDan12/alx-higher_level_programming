#!/usr/bin/python3
# 2-matrix_divided.py
"""Define a function that divides all elements in a matrix"""

def matrix_divided(matrix, div):
    """Divise the elements of a matrix.

    Args:
        matrix (list): list of lists of int and float.
        div (int/float): Divisor.
    Raises:
        TypeError: if the matrix contains non-number.
        TypeError: matrix contains rows of different sizes
        TypeError: Div is not an int or float.
        ZeroDivisionError: Div is 0.
    Returns:
        New matrix giving the resulat of the division.
    """
    if (not isinstance(matrix, list) or matrix == [] or not all(isinstance(row, list) for row in matrix) or not all((isinstance(ele, int) or isinstance(ele, float))
        for ele in [num for row in matrix for num in row])):
        raise TypeError("matrix must be a matrix (list of lists) of integers/floats")

    if not all(len(row) == len(matrix[0]) for row in matrix):
        raise TypeError("Each row of the matrix must have the same size")

    if not isinstance(div, int) and not isinstance(div, float):
        raise TypeError("div must be a number")

    if div == 0:
        raise ZeroDivisionError("division by zero")

    return ([list(map(lambda x: round(x / div, 2), row)) for row in matrix])
