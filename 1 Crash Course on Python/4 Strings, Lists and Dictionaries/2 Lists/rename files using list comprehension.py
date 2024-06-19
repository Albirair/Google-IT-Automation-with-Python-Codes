#!/usr/bin/env python3
filenames = ["program.c", "stdio.hpp",
             "sample.hpp", "a.out", "math.hpp", "hpp.out"]
new_filenames = [filename[:-2] if filename.endswith(
    '.hpp') else filename for filename in filenames]
print(new_filenames)