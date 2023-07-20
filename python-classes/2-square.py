#!/usr/bin/python3
"""python3 -c 'print(__import__("my_module").__doc__)'"""


class Square:
    """python3 -c 'print(__import__("my_module").MyClass.__doc__)'"""
    pass

    def __init__(self, size=0):
        self._Square__size = size
        size_type =type(size)
        if size_type != 'int':
            print("size must be an integer")
        elif size < 0:
            print("size must be >= 0")
