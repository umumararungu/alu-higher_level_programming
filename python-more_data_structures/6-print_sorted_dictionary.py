#!/usr/bin/python3
def print_sorted_dictionary(a_dictionary):
    value = sorted(a_dictionary.keys())
    for key in value:
        print("{}: {}".format(key, a_dictionary[key]))
