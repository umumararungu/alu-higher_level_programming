#!/usr/bin/python3
"""python3 -c 'print(__import__("my_module").__doc__)'"""


class Mylist(list):
    """python3 -c 'print(__import__("my_module").MyClass.__doc__)'"""
    pass
 
    def append(self, value):
        """+python3 -c 'print(__import__("my_module").my_function.__doc__)'"""
        super().append(value)
        self.sort()

    def print_sorted(self):
        """+python3 -c 'print(__import__("my_module").my_function.__doc__)'"""
        print(sorted(self))