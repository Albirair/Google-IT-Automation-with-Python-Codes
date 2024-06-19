#!/usr/bin/env python3
from multiprocessing import Pool
import subprocess
import os
src = os.path.join(os.getenv("HOME"), "data/prod")
dest = os.path.join(os.getenv("HOME"), "data/prod_backup")
def backup(f):
    subprocess.call(["rsync", "-arq", os.path.join(src, f), dest])
if __name__ == "__main__":
    list_of_files = os.listdir(src)
    all_files = []
    for value in list_of_files:
        full_path = os.path.join(src, value)
        all_files.append(full_path)
    with Pool(len(all_files)) as pool:
        pool.map(backup, all_files)