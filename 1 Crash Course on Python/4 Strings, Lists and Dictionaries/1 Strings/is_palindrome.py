#!/usr/bin/env python3
def is_palindrome(input_string):
    new_string = ""
    reverse_string = ""
    for letter in input_string:
        if letter != " ":
            new_string = new_string + letter
            reverse_string = letter + reverse_string
    if new_string.lower() == reverse_string.lower():
        return True
    return False
print(is_palindrome("Never Odd or Even"))
print(is_palindrome("abc"))
print(is_palindrome("kayak"))