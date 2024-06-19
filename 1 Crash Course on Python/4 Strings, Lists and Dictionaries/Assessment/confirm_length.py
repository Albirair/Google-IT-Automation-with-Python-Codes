#!/usr/bin/env python3
def confirm_length(word):
    if len(word) > 0:
        return len(word)
    else:
        return 0
print(confirm_length("a"))
print(confirm_length("This is a long string"))
print(confirm_length("Monday"))
print(confirm_length(""))