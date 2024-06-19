#!/usr/bin/env python3
def even_numbers(n):
    count = 0
    current_number = 0
    while current_number <= n:
        if current_number % 2 == 0:
            count += 1
        current_number += 1
    return count
print(even_numbers(25))
print(even_numbers(144))
print(even_numbers(1000))
print(even_numbers(0))