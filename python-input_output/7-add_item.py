#!/usr/bin/python3

"""Add all arguments to a Python list and save them to a file."""

import sys
import os.path
from os import path
from save_to_json_file import save_to_json_file
from load_from_json_file import load_from_json_file

def add_items_to_list(filename, *args):
    """"python3 -c 'print(__import__("my_module").my_function.__doc__)'""""
    my_list = []
    if path.exists(filename):
        my_list = load_from_json_file(filename)
    my_list.extend(args)
    save_to_json_file(my_list, filename)

if __name__ == "__main__":
    filename = "add_item.json"
    args = sys.argv[1:]
    add_items_to_list(filename, *args)
