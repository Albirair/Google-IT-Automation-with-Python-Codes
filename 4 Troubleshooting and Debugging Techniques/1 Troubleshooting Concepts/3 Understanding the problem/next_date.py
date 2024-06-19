#!/usr/bin/env python3
import datetime
from datetime import date
def add_year(date_obj):
    try:
        new_date_obj = date_obj.replace(year=date_obj.year + 1)
    except ValueError:
        new_date_obj = date_obj.replace(year=date_obj.year + 4)
    return new_date_obj
def next_date(date_string):
    date_obj = datetime.datetime.strptime(date_string, r"%Y-%m-%d")
    next_date_obj = add_year(date_obj)
    next_date_string = next_date_obj.strftime("%Y-%m-%d")
    return next_date_string
today = date.today()
print(next_date(str(today)))
print(next_date("2021-01-01"))
print(next_date("2020-02-29"))