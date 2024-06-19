#!/usr/bin/env python3
def even_numbers(first, last):
    return [even for even in range(first, last) if even % 2 == 0]
print(even_numbers(4, 14))
print(even_numbers(0, 9))
print(even_numbers(2, 7))