#!/usr/bin/python3
def max_integer(my_list=[]):
    a = []
    if my_list == a:
        return None
    else:
         large_number = None
            for number in my_list:
                if large_number is None or large_number < number:
                    print(number)
