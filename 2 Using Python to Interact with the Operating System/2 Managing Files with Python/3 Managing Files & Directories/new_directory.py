#!/usr/bin/env python3
import os
def new_directory(directory, filename):
    if os.path.isdir(directory) == False:
        os.mkdir(directory)
    os.chdir(directory)
    with open(filename, 'x') as file:
        pass
    return os.listdir()
print(new_directory("PythonPrograms", "script.py"))