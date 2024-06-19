#!/usr/bin/env python3
def clothing_type(temp):
    if temp > 65:
        clothing = "T-Shirt"
    elif temp > 50:
        clothing = "Sweatshirt"
    elif temp > 32:
        clothing = "Jacket"
    else:
        clothing = "Heavy Coat"
    return clothing
print(clothing_type(72))
print(clothing_type(55))
print(clothing_type(65))
print(clothing_type(50))
print(clothing_type(45))
print(clothing_type(32))
print(clothing_type(0))