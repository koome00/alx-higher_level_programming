#!/usr/bin/python3
def multiple_returns(sentence):
    length = len(sentence)
    first = sentence[0]
    if length == 0:
        tuple_a = tuple((length, None))
        return tuple_a
    else:
        tuple_a = tuple((length, first))
        return tuple_a
