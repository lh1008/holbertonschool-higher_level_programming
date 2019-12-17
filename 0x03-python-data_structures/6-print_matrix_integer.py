#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    i = 0
    for r in matrix:
        for value in r:
            if i == 0:
                print('{:d}'.format(value), end='')
            else:
                print('{:2d}'.format(value), end='')
            i = i + 1
        i = 0
        print()
