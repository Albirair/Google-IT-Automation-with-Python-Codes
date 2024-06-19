#!/usr/bin/env python3
def is_power_of(number, base):
    if number < base:
        return number == 1
    return is_power_of(number / base, base)
print(is_power_of(8, 2))
print(is_power_of(64, 4))
print(is_power_of(70, 10))