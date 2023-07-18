#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    if matrix != 0:
        for row in matrix:
            for col in row:
                square = (matrix[col]pow(2))
                return square
