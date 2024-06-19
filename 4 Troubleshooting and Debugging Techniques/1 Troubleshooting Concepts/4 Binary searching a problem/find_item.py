#!/usr/bin/env python3
def find_item(list, item):
    if len(list) == 0:
        return False
    list.sort()
    middle = len(list)//2
    if list[middle] == item:
        return True
    if item < list[middle]:
        return find_item(list[:middle], item)
    return find_item(list[middle+1:], item)
list_of_names = ["Parker", "Drew", "Cameron", "Logan",
                 "Alex", "Chris", "Terry", "Jamie", "Jordan", "Taylor"]
print(find_item(list_of_names, "Alex"))
print(find_item(list_of_names, "Andrew"))
print(find_item(list_of_names, "Drew"))
print(find_item(list_of_names, "Jared"))