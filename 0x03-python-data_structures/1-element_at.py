#!/usr/bin/python3
def element_at(my_list, idx):
    list_len = len(my_list)
    if idx < 0:
        print("None")
    elif idx > (list_len - 1):
        print("None")
    else:
        num = my_list[idx]
        return num
