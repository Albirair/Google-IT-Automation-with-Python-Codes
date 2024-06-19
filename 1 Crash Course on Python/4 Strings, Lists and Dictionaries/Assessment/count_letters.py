#!/usr/bin/env python3
def count_letters(text):
    dictionary = {}
    for c in text.lower():
        if c.isalpha():
            if c not in dictionary:
                dictionary[c] = 0
            dictionary[c] += 1
    return dictionary
print(count_letters("AaBbCc"))
print(count_letters("Math is fun! 2+2=4"))
print(count_letters("This is a sentence."))