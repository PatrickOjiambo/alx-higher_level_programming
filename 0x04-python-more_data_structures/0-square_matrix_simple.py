#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    matrix2 = list(map(lambda row: list(map(lambda x: x ** 2, row)), matrix))
    return matrix2
