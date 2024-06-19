#!/usr/bin/env python3
def counter(start, stop):
    if start > stop:
        return_string = "Counting down: "
        while start >= stop:
            return_string += str(start)
            if start > stop:
                return_string += ","
            start -= 1
    else:
        return_string = "Counting up: "
        while start <= stop:
            return_string += str(start)
            if start < stop:
                return_string += ","
            start += 1
    return return_string
print(counter(1, 10))
print(counter(2, 1))
print(counter(5, 5))