#!/usr/bin/python3
def uniq_add(my_list=[]):
    uni = list(dict.fromkeys(my_list))
    print("Result: {:d}".format(uni))
