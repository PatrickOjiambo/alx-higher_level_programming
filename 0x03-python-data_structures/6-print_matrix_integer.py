#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    if len(matrix) == 0:
        print("")
    else:
        for x, y, z in matrix:
            print("{} {} {}".format(x, y, z))


