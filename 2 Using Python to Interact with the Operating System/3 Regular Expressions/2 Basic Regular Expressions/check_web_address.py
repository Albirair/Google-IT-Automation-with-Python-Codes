#!/usr/bin/env python3
import re
def check_web_address(text):
    pattern = r"^[a-zA-Z0-9_.+-]+\.[a-zA-Z0-9]+$"
    result = re.search(pattern, text)
    return result != None
print(check_web_address("gmail.com"))
print(check_web_address("www@google"))
print(check_web_address("www.Coursera.org"))
print(check_web_address("web-address.com/homepage"))
print(check_web_address("My_Favorite-Blog.US"))