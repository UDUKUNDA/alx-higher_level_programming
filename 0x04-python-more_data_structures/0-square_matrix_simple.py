#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    nMatt = matrix.copy()

    for i in range(len(matrix)):
        nMatt[i] = list(map(lambda x: x**2, matrix[i]))

    return (nMatt)
