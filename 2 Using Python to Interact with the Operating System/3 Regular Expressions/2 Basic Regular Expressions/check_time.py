#!/usr/bin/env python3
import re
def check_time(text):
    pattern = r"(\d|1[012]):[0-5]\d ?[aApP][mM]"
    result = re.search(pattern, text)
    return result != None
print(check_time("12:45pm"))
print(check_time("9:59 AM"))
print(check_time("6:60am"))
print(check_time("five o'clock"))
print(check_time("6:02 am"))
print(check_time("6:02km"))