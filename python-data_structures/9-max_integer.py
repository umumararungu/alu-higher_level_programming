#!/usr/bin/python3
def max_integer(my_list=[]):
    if my_list == []:
        return None
    else:
        large_number = sorted(my_list)[-1]
        return large_number
