#!/usr/bin/env python3
import os
def create_python_script(filename):
    comments = "# Start of a new Python program"
    file = open(filename, 'w')
    file.write(comments)
    file.close()
    filesize = os.path.getsize(filename)
    return filesize
print(create_python_script("program.py"))