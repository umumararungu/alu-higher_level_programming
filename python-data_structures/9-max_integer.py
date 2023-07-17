#!/usr/bin/python3
def max_integer(my_list=[]):
    a = []
    if my_list == a:
        return None
    else:
        print(all([isinstance(item, int) for item in my_list]))
