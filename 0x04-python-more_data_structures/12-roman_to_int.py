#!/usr/bin/python3
def roman_to_int(roman_string):
    roman = {'I':1, 'V':5, 'X':10, 'L':50, 'C':100, 'D':500, 'M':1000}
    num = 0
    nine = "IX"
    x = 0
    roman_string = list(roman_string)
    if roman_string != None:
        if nine in roman_string:
            roman_string[x:x+2] = nine
            list1 = roman_string[:x]
            list2 = roman_string[x+1:]
            num1 = 0
            num2 = 0
            if roman_string == nine:
                num = 9
            else:
                for letter in list1:
                    for i, j in roman.items():
                        if letter == i:
                            num1 += j
                        else:
                            num = 0
                for letter in list2:
                    for i, j in roman.items():
                        if letter == i:
                            num2 += j
                        else:
                            num2 = 0
            if num1 == 0 and num2 == 0:
                num = 9
            else:
                num = str(num1) + str("9") + str(num2)
                num = int(num)
        else:
            for letter in roman_string:
                for i, j in roman.items():
                    if letter == i:
                        num += j
    else:
        num = 0
    return num
