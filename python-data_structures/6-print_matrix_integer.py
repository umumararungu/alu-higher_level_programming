#!/usr/bin/python3
def print_matrix_interger(matrix=[[]]):
    for row in matrix:
        for col in range(len(row)):
            print("{:d}".format(row[col]), end="")
            if col != len(row) - 1:
                print(" ", end="")
        print()
