#!/usr/bin/env python3
def biography_list(people):
    for person in people:
        name, age, profession = person
        print("{} is {} years old and works as {}".format(name, age, profession))
biography_list([("Ira", 30, "a Chef"), ("Raj", 35, "a Lawyer"),
               ("Maria", 25, "an Engineer")])