#!/usr/bin/python3
""" This module defines a function called matrix_divided"""


def matrix_divided(matrix, div):
    """ A function that devides a matrix with a given number

    Args:
        matrix(list): The matrix to be divided
        div: A number that divides the matrix
    Raises:
        TypeError: if matrix is not a list of lists of integers or floats
        TypeError: if each row of the matrix must be of the same size
        TypeError: if div is not an integer or a float
        ZeroDivisionError: if div is 0
    Returns:
        The new matrix
    """

    error_1 = "matrix must be a matrix (list of lists) of integers/floats"
    error_2 = "Each row of the matrix must have the same size"
    error_3 = "div must be a number"
    error_4 = "division by zero"
    if not isinstance(div, (int, float)):
        raise TypeError(error_3)
    if div == 0:
        raise ZeroDivisionError(error_4)
    if not isinstance(matrix, list):
        raise TypeError(error_1)
    for mini_list in matrix:
        if not isinstance(mini_list, list):
            raise TypeError(error_1)
        if len(mini_list) != len(matrix[0]):
            raise TypeError(error_2)
        for element in mini_list:
            if not isinstance(element, (int, float)):
                raise TypeError(error_1)
    new_matrix = []
    for mini_list in matrix:
        new_mini_list = []
        for element in mini_list:
            new_element = round(element / div, 2)
            new_mini_list.append(new_element)
        new_matrix.append(new_mini_list)
    return new_matrix
