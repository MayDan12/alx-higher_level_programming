#!/usr/bin/python3
"""This Defines a Pascal's Triangle function."""


def pascal_triangle(n):
    """This Represent Pascal's Triangle of size n.

    This Returns a list of lists of integers representing the triangle.
    """
    if n <= 0:
        return []

    triangle = [[1]]
    while len(triangle) != n:
        tris = triangle[-1]
        tmps = [1]
        for i in range(len(tris) - 1):
            tmps.append(tris[i] + tris[i + 1])
        tmps.append(1)
        triangle.append(tmps)
    return triangle
