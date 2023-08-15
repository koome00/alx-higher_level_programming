#!/usr/bin/python3
def max_integer(my_list=[]):
    length = len(my_list)
    if length == 0:
        return None
    else:
        biggest = my_list[length - 1]
        for num in my_list:
            if num > biggest:
                biggest = num
        return biggest
