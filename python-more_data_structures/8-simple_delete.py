#!/usr/bin/python3
def update_dictionary(a_dictionary, key, value):
    if key in a_dictionary:
        del a_dictionary[value]
    return a_dictionary
