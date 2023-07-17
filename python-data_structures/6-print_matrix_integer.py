#!/usr/bin/python3
def print_matrix_interger(matrix=[[]]):
    for row in matrix:
        for col in range(len(row)):
            print("{:d}".format(col), end=" " if col != row[-1] else "")
        print()
