#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
number = str(number)
last_digit = number[-1]
last_digit1 = int(last_digit)
if last_digit1 > 5:
    print("Last digit of {:s} is {:d} and is greater than 5"
          .format(number, last_digit1))
elif last_digit1 == 0:
    print("Last digit of {:s} is {:d} and is 0"
          .format(number, last_digit1))
else:
    print("Last digit of {:s} is {:d} and is less than 6 and not 0"
          .format(number, last_digit1))
