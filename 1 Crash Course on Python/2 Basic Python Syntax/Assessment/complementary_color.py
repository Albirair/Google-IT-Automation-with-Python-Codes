#!/usr/bin/env python3
def complementary_color(color):
    if color == "blue":
        complement = "orange"
    elif color == "yellow":
        complement = "purple"
    elif color == "red":
        complement = "green"
    else:
        complement = "unknown"
    return complement
print(complementary_color("blue"))
print(complementary_color("yellow"))
print(complementary_color("red"))
print(complementary_color("black"))
print(complementary_color("Blue"))
print(complementary_color(""))