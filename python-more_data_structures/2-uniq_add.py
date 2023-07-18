#!/usr/bin/python3
def uniq_add(my_list=[]):
    uni = set()
    sum = 0
    for number in my_list:
        if number not in uni:
            uni.add(number)
            sum += number
    return sum
