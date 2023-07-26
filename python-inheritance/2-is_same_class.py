#!/usr/bin/python3
'''python3 -c 'print(__import__("my_module").__doc__)'''


def is_same_class(obj, a_class):
    '''+python3 -c 'print(__import__("my_module").my_function.__doc__)'''
    if not isinstance(obj, a_class):
        return False
    else:
        return True
