#!/usr/bin/env python3
filenames = ["program.c", "stdio.hpp",
             "sample.hpp", "a.out", "math.hpp", "hpp.out"]
new_filenames = []
for filename in filenames:
    if filename.endswith("hpp"):
        new_filenames.append(filename[:-2])
    else:
        new_filenames.append(filename)
print(new_filenames)