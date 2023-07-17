#!/usr/bin/python3
def max_integer(my_list=[]):
    for number in my_list:
        large_number = None
        if large_number is None or large_number < number:
            large_number = number
            print(large_number)
