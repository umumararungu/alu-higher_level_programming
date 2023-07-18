#!/usr/bin/python3
def common_elements(set_1, set_2):
    new_set = []
    for item_1 in set_1:
        for item_2 in set_2:
            if set_1[item_1] == set_2[item_2]:
                new_item = item_1
                new_set.add(new_item)

    return new_set
