#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
        a = len(tuple_a)
        b = len(tuple_b)
        sum1 = (tuple_a[0] if a > 0 else 0) + (tuple_b[0] if b > 0 else 0)
        sum2 = (tuple_a[1] if a >= 2 else 0) + (tuple_b[1] if b >= 2 else 0)
        new_tuple = tuple((sum1,sum2))
        return new_tuple
