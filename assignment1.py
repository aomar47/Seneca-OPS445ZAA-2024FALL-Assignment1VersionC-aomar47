#!/usr/bin/env python3


'''
OPS445 Assignment 1
Program: assignment1.py
The python code in this file is original work written by
"Azra Omar". No code in this file is copied from any other source
except those provided by the course instructor, including any person,
textbook, or on-line resource. I have not shared this python script
with anyone or anything except for submission for grading. I understand
that the Academic Honesty Policy will be enforced and
violators will be reported and appropriate action will be taken.

Author: Azra Omar
Semester: Fall 2024
Description: This is Assignment 1 Submission.   
'''

import sys

def day_of_week(date: str) -> str:
    # Get the day of the week for a date.
    day, month, year = (int(x) for x in date.split('/'))
    days = ['Sun', 'Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat']
    offset = {1:0, 2:3, 3:2, 4:5, 5:0, 6:3, 7:5, 8:1, 9:4, 10:6, 11:2, 12:4}
    if month < 3:
        year -= 1
    num = (year + year//4 - year//100 + year//400 + offset[month] + day) % 7
    return days[num]

def leap_year(year: int) -> bool:
    # Check if a year is a leap year.
    return year % 4 == 0 and (year % 100 != 0 or year % 400 == 0)

def mon_max(month: int, year: int) -> int:
    # Get max days in a month.
    mon_dict = {1: 31, 2: 28, 3: 31, 4: 30, 5: 31, 6: 30,
                7: 31, 8: 31, 9: 30, 10: 31, 11: 30, 12: 31}
    return 29 if month == 2 and leap_year(year) else mon_dict[month]

def after(date: str) -> str:
    # Get the next day's date.
    day, mon, year = (int(x) for x in date.split('/'))
    day += 1
    if day > mon_max(mon, year):
        day = 1
        mon += 1
        if mon > 12:
            mon = 1
            year += 1
    return f"{day:02}/{mon:02}/{year}"

def before(date: str) -> str:
    # Get the previous day's date.
    day, mon, year = (int(x) for x in date.split('/'))
    day -= 1
    if day < 1:
        mon -= 1
        if mon < 1:
            mon = 12
            year -= 1
        day = mon_max(mon, year)
    return f"{day:02}/{mon:02}/{year}"

def usage():
    # Show usage info and exit.
    print(f"Usage: {sys.argv[0]} DD/MM/YYYY NN")
    sys.exit(1)

def valid_date(date: str) -> bool:
    # Check if a date is valid.
    try:
        day, month, year = (int(x) for x in date.split('/'))
    except ValueError:
        return False
    if not (1 <= month <= 12 and 1 <= day <= 31 and year >= 0):
        return False
    if day > mon_max(month, year):
        return False
    return True

def day_iter(start_date: str, num: int) -> str:
    # Get the date after adding/subtracting days.
    current_date = start_date
    if num > 0:
        for _ in range(num):
            current_date = after(current_date)
    elif num < 0:
        for _ in range(abs(num)):
            current_date = before(current_date)
    return current_date

if __name__ == "__main__":
    # Validate input arguments.
    if len(sys.argv) != 3:
        usage()
   
    start_date = sys.argv[1]
    if not valid_date(start_date):
        print("Error: Invalid start date.")
        usage()
   
    try:
        num = int(sys.argv[2])
    except ValueError:
        print("Error: Second argument must be an integer.")
        usage()
   
    # Print the end date.
    end_date = day_iter(start_date, num)
    print(f"The end date is {day_of_week(end_date)}, {end_date}.")
