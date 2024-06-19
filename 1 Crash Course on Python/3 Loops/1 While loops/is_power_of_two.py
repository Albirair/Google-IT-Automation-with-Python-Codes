#!/usr/bin/env python3
def is_power_of_two(number):
    if number == 0:
        return False
    while number % 2 == 0:
        number = number / 2
    if number == 1:
        return True
    return False
print(is_power_of_two(0))
print(is_power_of_two(1))
print(is_power_of_two(8))
print(is_power_of_two(9))