#!/usr/bin/python3
"""python3 -c 'print(__import__("my_module").__doc__)'"""


def text_indentation(text):
    """python3 -c 'print(__import__("my_module").my_function.__doc__)'"""

    if not isinstance(text, str):
        raise TypeError("text must be a string")

    c = 0
    while c < len(text) and text[c] == ' ':
        c += 1

    while c < len(text):
        print(text[c], end="")
        if text[c] == "\n" or text[c] in ".?:":
            if text[c] in ".?:":
                print("\n")
            c += 1
            while c < len(text) and text[c] == ' ':
                c += 1
            continue
        c += 1
