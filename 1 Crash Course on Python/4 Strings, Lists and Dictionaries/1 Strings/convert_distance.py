#!/usr/bin/env python3
def convert_distance(miles):
    km = miles * 1.6
    result = "{} miles equals {:.1f} km".format(miles, km)
    return result
print(convert_distance(12))
print(convert_distance(5.5))
print(convert_distance(11))