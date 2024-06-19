#!/usr/bin/env python3
def format_address(address_string):
    house_number = ""
    street_name = ""
    address_parts = address_string.split()
    for address_part in address_parts:
        if house_number == "":
            house_number = address_part
        else:
            street_name += address_part + " "
    street_name = street_name.strip()
    return f"House number {house_number} on a street named {street_name}"
print(format_address("123 Main Street"))
print(format_address("1001 1st Ave"))
print(format_address("55 North Center Drive"))