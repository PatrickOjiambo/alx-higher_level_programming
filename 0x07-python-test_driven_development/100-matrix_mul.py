#!/usr/bin/python3
"""
This module contains a function that multiplies 
2 matrices nd outputes the result
"""


def matrix_mul(m_a, m_b):
    """
    Multiplies two matrices.

    >>> matrix_mul([[1, 2, 3], [4, 5, 6]], [[7, 8], [9, 10], [11, 12]])
    [[58, 64], [139, 154]]

    >>> matrix_mul([[1, 2, 3]], [[4], [5], [6]])
    [[32]]

    >>> matrix_mul([[1, 2], [3, 4]], [[5, 6, 7], [8, 9, 10]])
    Traceback (most recent call last):
        ...
    ValueError: m_a and m_b can't be multiplied

    >>> matrix_mul([[1, 2], [3, 4]], [[5, 6], [7, 'eight']])
    Traceback (most recent call last):
        ...
    TypeError: m_b should contain only integers or floats

    >>> matrix_mul([[1, 2], [3, 4]], 'invalid')
    Traceback (most recent call last):
        ...
    TypeError: m_b must be a list

    >>> matrix_mul([[1, 2], [3, 4]], [])
    Traceback (most recent call last):
        ...
    ValueError: m_b can't be empty

    >>> matrix_mul([[1, 2], [3, 4]], [[]])
    Traceback (most recent call last):
        ...
    ValueError: m_b can't be empty

    >>> matrix_mul([], [[1, 2], [3, 4]])
    Traceback (most recent call last):
        ...
    ValueError: m_a can't be empty

    >>> matrix_mul('invalid', [[1, 2], [3, 4]])
    Traceback (most recent call last):
        ...
    TypeError: m_a must be a list

    >>> matrix_mul([[1, 2], [3, 4]], [[5, 6], [7]])
    Traceback (most recent call last):
        ...
    TypeError: each row of m_b must be of the same size

    >>> matrix_mul([[1, 2], [3, 4]], [[5, 6], [7, 8, 9]])
    Traceback (most recent call last):
        ...
    TypeError: each row of m_b must be of the same size

    >>> matrix_mul([[1, 2], [3, 4]], [[5, 6], [7, 8]])
    [[19, 22], [43, 50]]
    """
    if not isinstance(m_a, list) or not isinstance(m_b, list):
        raise TypeError("m_a must be a list or m_b must be a list")
    
    if not all(isinstance(row, list) for row in m_a) or not all(isinstance(row, list) for row in m_b):
        raise TypeError("m_a must be a list of lists or m_b must be a list of lists")
    
    if not m_a or not m_b:
        raise ValueError("m_a can't be empty or m_b can't be empty")
    
    if any(not isinstance(num, (int, float)) for row in m_a for num in row) or any(not isinstance(num, (int, float)) for row in m_b for num in row):
        raise TypeError("m_a should contain only integers or floats or m_b should contain only integers or floats")
    
    row_sizes_a = [len(row) for row in m_a]
    row_sizes_b = [len(row) for row in m_b]
    if any(size != row_sizes_a[0] for size in row_sizes_a) or any(size != row_sizes_b[0] for size in row_sizes_b):
        raise TypeError("each row of m_a must be of the same size or each row of m_b must be of the same size")
    
    if len(row_sizes_a) != len(m_b[0]):
        raise ValueError("m_a and m_b can't be multiplied")
    
    # Multiply matrices
    result = []
    for i in range(len(m_a)):
        row = []
        for j in range(len(m_b[0])):
            element = sum(m_a[i][k] * m_b[k][j] for k in range(len(m_b)))
            row.append(element)
        result.append(row)
    
    return result
