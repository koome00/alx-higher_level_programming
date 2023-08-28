#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    try:
        lst = "".join(map(str, my_list[:x]))
        print(lst)
        count = 0
        for item in my_list:
            count += 1
        return count
    except IndexError:
        return x
