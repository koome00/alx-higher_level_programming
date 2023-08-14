#!/usr/bin/python3
def max_integer(my_list=[]):
    length = len(my_list)
    if length == 0:
        return None
    else:
        while length > 0:
            biggest = 0
            for num in my_list:
                if num > biggest:
                    biggest = num
            return biggest
