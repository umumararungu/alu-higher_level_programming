#!/usr/bin/python3
def common_elements(set_1, set_2):
    new_set = []
    for item_1 in set_1:
        new_value = item_1
        for item_2 in set_2:
            if set_1[new_value] == set_2[item_2]:
                new_set.add(new_value)

    return new_set
