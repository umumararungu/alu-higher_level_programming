#!/usr/bin/python3
"""Add all arguments to a Python list and save them to a file."""
import sys
from os import path
from typing import List
save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file

def add_to_list_and_save(arguments: List[str]):
    filename = "add_item.json"
    my_list = []

    if path.exists(filename):
        my_list = load_from_json_file(filename)

    my_list.extend(arguments)
    save_to_json_file(my_list, filename)

if __name__ == "__main__":
    arguments = sys.argv[1:]
    add_to_list_and_save(arguments)