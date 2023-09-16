#!/usr/bin/python3
""" A module that defines a function called matrix_mul """


def matrix_mul(m_a, m_b):
    """ A function that multiplies 2 matrices
    Args:
        m_a: the first matrix
        m_b: the second matrix
    Returns:
        The new matrix which is the multiple of the two given matrices
    """
    if not isinstance(m_a, list):
        raise TypeError("m_a must be a list")
    if not isinstance(m_b, list):
        raise TypeError("m_b must be a list")
    for i in range(len(m_a)):
        if not isinstance(m_a[i], list):
            raise TypeError("m_a must be a list of lists")
    for i in range(len(m_b)):
        if not isinstance(m_b[i], list):
            raise TypeError("m_b must be a list of lists")
    if m_a == [] or m_a == [[]]:
        raise ValueError("m_a can't be empty")
    if m_b == [] or m_b == [[]]:
        raise ValueError("m_b can't be empty")
    for row in m_a:
        for element in row:
            if not isinstance(element, (int, float)):
                raise TypeError("m_a should contain only integers or floats")
    for row in m_b:
        for element in row:
            if not isinstance(element, (int, float)):
                raise TypeError("m_b should contain only integers or floats")
    for i in range(len(m_a)):
        if len(m_a[i]) != len(m_a[0]):
            raise TypeError("each row of m_a must be of the same size")
    for i in range(len(m_b)):
        if len(m_b[i]) != len(m_b[0]):
            raise TypeError("each row of m_b must be of the same size")
    if len(m_a[0]) != len(m_b):
        raise ValueError("m_a and m_b can't be multiplied")

    row_a = len(m_a)
    row_b = len(m_b)
    column_a = len(m_a[0])
    column_b = len(m_b[0])

    new_matrix = []
    for i in range(len(m_a)):
        row = []
        for j in range(len(m_b[0])):
            element = 0
            for k in range(len(m_a[0])):
                element += m_a[i][k] * m_b[k][j]
            row.append(element)
        new_matrix.append(row)
    return new_matrix
