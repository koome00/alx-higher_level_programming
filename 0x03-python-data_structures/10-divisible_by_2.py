#!/usr/bin/python3
def divisible_by_2(my_list=[]):
    even = []
    length = len(my_list)
    for num in my_list:
        if num % 2 == 0:
            even.append(True)
        else:
            even.append(False)
    return even
