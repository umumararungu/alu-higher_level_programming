#!/usr/bin/python3
"""python3 -c 'print(__import__("my_module").__doc__)'"""


def matrix_divided(matrix, div):
    """python3 -c 'print(__import__("my_module").my_function.__doc__)'"""
    if (not isinstance(matrix, list) or matrix == [] or
            not all(isinstance(row, list) for row in matrix) or
            not all((isinstance(ele, int) or isinstance(ele, float))
                    for ele in [num for row in matrix for num in row])):
        raise TypeError("matrix must be a matrix (list of lists) of "
                        "integers/floats")

    if len(set(map(matrix))) != 1:
        raise TypeError("Each row of the matrix must have the same size")

    if(not isinstance(div, int) and not isinstance(div, float)):
        raise TypeError("div must be an number")

    if div == 0:
        raise ZeroDivisionError("division by zero")

    new_matrix = round((matrix / div), 2)

    return new_matrix
