#!/usr/bin/env python3
import re
def correct_function(text):
    result = re.search(r" \d{5}(-\d{4})?", text)
    return result is not None
def check_zip_code(text):
    return correct_function(text)
print(check_zip_code("The zip codes for New York are 10001 thru 11104."))
print(check_zip_code("90210 is a TV show"))
print(check_zip_code("Their address is: 123 Main Street, Anytown, AZ 85258-0001."))
print(check_zip_code(
    "The Parliament of Canada is at 111 Wellington St, Ottawa, ON K1A0A9."))