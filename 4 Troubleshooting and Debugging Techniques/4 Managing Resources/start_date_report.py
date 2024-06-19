#!/usr/bin/env python3
import csv
import datetime
import requests
from operator import itemgetter
def get_file_lines(url):
    """Returns the lines contained in the file at the given URL"""
    response = requests.get(url, stream=True)
    lines = []
    for line in response.iter_lines():
        lines.append(line.decode("UTF-8"))
    return lines
def get_start_date():
    """Interactively get the start date to query for."""
    print()
    print('Getting the first start date to query for.')
    print()
    print('The date must be greater than Jan 1st, 2018')
    year = int(input('Enter a value for the year: '))
    month = int(input('Enter a value for the month: '))
    day = int(input('Enter a value for the day: '))
    print()
    return datetime.datetime(year, month, day)
def list_newer(start_date):
    FILE_URL = "https://storage.googleapis.com/gwg-content/gic215/employees-with-date.csv"
    data = get_file_lines(FILE_URL)
    reader = csv.reader(data[1:])
    employees = list(reader)
    employees.sort(key=itemgetter(3))
    counter = 0
    while datetime.datetime.strptime(employees[counter][3], '%Y-%m-%d') < start_date and counter < len(employees):
        counter += 1
    while counter < len(employees):
        current_date = employees[counter][3]
        con = []
        while counter < len(employees) and current_date == employees[counter][3]:
            con.append(employees[counter])
            counter += 1
        print("Started on {}: {}".format(current_date, con))
def main():
    start_date = get_start_date()
    list_newer(start_date)
if __name__ == "__main__":
    main()