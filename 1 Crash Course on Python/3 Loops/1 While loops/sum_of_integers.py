#!/usr/bin/env python3
def sum_of_integers(n):
    if n < 1:
        return 0
    i = 1
    sum = 0
    while i <= n:
        sum = sum + i
        i = i + 1
    return sum
print(sum_of_integers(3))
print(sum_of_integers(4))
print(sum_of_integers(5))