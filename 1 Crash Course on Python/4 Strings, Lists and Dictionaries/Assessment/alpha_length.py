#!/usr/bin/env python3
def alpha_length(string):
    count_alpha = 0
    for c in string:
        if c.isalpha():
            count_alpha += 1
    return count_alpha
print(alpha_length("This has 1 number in it"))
print(alpha_length("Thisisallletters"))
print(alpha_length("This one has punctuation!"))