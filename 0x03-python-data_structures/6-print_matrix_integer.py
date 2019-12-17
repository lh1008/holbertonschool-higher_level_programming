#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):

    for r in matrix:
        for value in r:
            print('{:d} '.format(value), end='')
        print()
