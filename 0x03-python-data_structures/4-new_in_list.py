#!/usr/bin/python3
def new_in_list(my_list, idx, element):
    len_list = len(my_list)
    if 0 > idx >= len_list:
        return my_list
    else:
        new_list = my_list.copy()
        new_list[idx] = element
        return new_list
