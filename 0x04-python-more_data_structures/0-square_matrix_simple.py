#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    """Thuis function do square matrix"""
    newest_matrix = matrix.copy()

    for g in range(len(matrix)):
        newest_matrix[g] = list(map(lambda x: x**2, matrix[g]))

    return (newest_matrix)
