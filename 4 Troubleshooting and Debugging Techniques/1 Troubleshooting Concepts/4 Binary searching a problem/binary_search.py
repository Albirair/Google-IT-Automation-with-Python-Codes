#!/usr/bin/env python3
def binary_search(list, key):
    list.sort()
    left = 0
    right = len(list) - 1
    while left <= right:
        middle = (left + right) // 2
        if list[middle] == key:
            return middle
        elif list[middle] > key:
            right = middle - 1
            print("Checking the left side")
        else:
            left = middle + 1
            print("Checking the right side")
    return -1
print(binary_search([10, 2, 9, 6, 7, 1, 5, 3, 4, 8], 1))
print(binary_search([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 5))