#!/usr/bin/env python3
def all_numbers(minimum, maximum):
    return_string = ""
    for i in range(minimum, maximum + 1):
        return_string += str(i) + " "
    return return_string.strip()
print(all_numbers(2, 6))
print(all_numbers(3, 10))
print(all_numbers(-1, 1))
print(all_numbers(0, 5))
print(all_numbers(0, 0))