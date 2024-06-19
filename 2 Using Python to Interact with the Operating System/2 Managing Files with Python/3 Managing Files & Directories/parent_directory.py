#!/usr/bin/env python3
import os
def parent_directory():
    relative_parent = os.path.join(".", "..")
    return os.path.abspath(relative_parent)
print(parent_directory())