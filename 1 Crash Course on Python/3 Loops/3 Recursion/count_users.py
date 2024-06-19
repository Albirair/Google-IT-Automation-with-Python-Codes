#!/usr/bin/env python3
def count_users(group):
    count = 0
    for member in get_members(group):
        if is_group(member):
            count += count_users(member)
        else:
            count += 1
    return count
print(count_users("sales"))
print(count_users("engineering"))
print(count_users("everyone"))