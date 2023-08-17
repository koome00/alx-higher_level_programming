#!/usr/bin/python3
def weight_average(my_list=[]):
    add = 0
    mul = 0
    sum1 = 0
    for row in my_list:
        mul = row[0] * row[1]
        sum1 += mul
        num = row[1]
        add += num
    aver = sum1/add
    return ever
