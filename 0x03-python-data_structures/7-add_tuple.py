#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
    addition = [0, 0]
    for i in range(2):
        if len(tuple_a) > i:
            addition[i] += tuple_a[i]
        if len(tuple_b) > i:
            addition[i] += tuple_b[i]
    c = (addition[0], addition[1])
    return (c)
