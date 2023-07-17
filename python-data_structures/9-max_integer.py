#!/usr/bin/python3
def max_integer(my_list=[]):
    if my_list == 0:
        return None
    else:
        print(all([isinstance(item, int) for item in my_list]))
