#!/usr/bin/python3
"""
7-add_item.py

Script that adds all arguments to a Python list and saves them to a JSON file.
"""

import sys
import os.path
from save_to_json_file import save_to_json_file
from load_from_json_file import load_from_json_file

def add_items_to_list(filename, *args):
    """
    Add all arguments to a Python list and save them to a JSON file.

    Args:
        filename (str): The name of the JSON file to save the list.
        *args (list): Variable-length argument list containing items to add to the list.

    Returns:
        list: The updated list containing all the items.
    """
    if os.path.isfile(filename):
        my_list = load_from_json_file(filename)
    else:
        my_list = []

    my_list.extend(args)
    save_to_json_file(filename, my_list)

    return my_list

if __name__ == "__main__":
    filename = "add_item.json"
    args = sys.argv[1:]
    updated_list = add_items_to_list(filename, *args)