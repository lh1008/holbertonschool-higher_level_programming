#!/usr/bin/python3
"""Module to divide a matrix"""

def matrix_divided(matrix, div):
    if not isinstance(matrix, (list)):
        raise TypeError("matrix must be a matrix (list of lists) of integers/floats")
    
