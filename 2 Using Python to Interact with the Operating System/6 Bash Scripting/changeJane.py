#!/usr/bin/env python3
import sys
import subprocess
old_files = sys.argv[1]
with open(old_files) as file:
    for line in file:
        new_name = line.strip().replace("jane", "jdoe")
        subprocess.run(["mv", line.strip(), new_name])