#!/usr/bin/python3
""" A module that defines a function called lazy_matrix_mul """


import numpy as np


def lazy_matrix_mul(m_a, m_b):
    """ A function that multiplies two matrices and return the result
    Args:
        m_a: the first matrix
        m_b: the second matrix
    Returns:
        The product of the two matrices
    """

    return np.matmul(m_a, m_b)
