#!/usr/bin/python3
from calculator_1 import add, sub, mul, div
a = 10
b = 5
add = add(a, b)
sub = sub(a, b)
mul = mul(a, b)
div = div(a, b)
print(f"{a:d} + {b:d} = {add:d}\n{a:d} - {b:d} = {sub:d}\n{a:d} * {b:d} = {mul:d}\n{a:d} / {b:d} = {div:d}")
