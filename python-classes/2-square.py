#!/usr/bin/python3
"""python3 -c 'print(__import__("my_module").__doc__)'"""


class Square:
    """python3 -c 'print(__import__("my_module").MyClass.__doc__)'"""
    pass

    def __init__(self, size=0):
        self._Square__size = size
        if not isinstance(size, int):
            raise TypeError("size must be integer")
        if size < 0:
            raise ValueError("size must be integer")
        