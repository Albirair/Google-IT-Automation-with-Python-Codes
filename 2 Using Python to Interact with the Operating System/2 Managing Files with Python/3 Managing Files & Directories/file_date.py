#!/usr/bin/env python3
import os
import datetime
def file_date(filename):
    _ = open(filename, 'w')
    timestamp = os.path.getmtime(filename)
    t = datetime.datetime.fromtimestamp(timestamp)
    return ("{}".format(t)[:10])
print(file_date("newfile.txt"))