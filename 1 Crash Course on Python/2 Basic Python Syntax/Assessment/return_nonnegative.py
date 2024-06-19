#!/usr/bin/env python3
def return_nonnegative(first_num, second_num):
    if first_num > second_num:
        result = first_num - second_num
    else:
        result = second_num - first_num
    return result
print(return_nonnegative(5, 5))
print(return_nonnegative(4, 5))
print(return_nonnegative(5, 3))
print(return_nonnegative(2, 5))
print(return_nonnegative(5, 0))
print(return_nonnegative(0, 5))