#!/usr/bin/env python3
import re
import csv
import operator
error = {}
per_user = {}
with open("syslog.log") as log:
    for line in log:
        user = re.search(r"\((.*)\)$", line)
        if user:
            if user[1] not in per_user:
                per_user[user[1]] = [0, 0]
            entry = re.search(r"ticky: ERROR ([\w' ]*) ", line)
            if entry:
                if entry[1] not in error:
                    error[entry[1]] = 0
                error[entry[1]] += 1
                per_user[user[1]][1] += 1
            else:
                per_user[user[1]][0] += 1
    error = sorted(error.items(), key=operator.itemgetter(1), reverse=True)
    per_user = sorted(per_user.items())
    error_message_csv = csv.writer(open("error_message.csv", "w"))
    error_message_csv.writerow(("Error", "Count"))
    error_message_csv.writerows(error)
    user_statistics_csv = csv.writer(open("user_statistics.csv", "w"))
    user_statistics_csv.writerow(("Username", "INFO", "ERROR"))
    for u in per_user:
        user_statistics_csv.writerow((u[0], u[1][0], u[1][1]))