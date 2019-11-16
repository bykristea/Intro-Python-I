"""
The Python standard library's 'calendar' module allows you to
render a calendar to your terminal.
https://docs.python.org/3.6/library/calendar.html

Write a program that accepts user input of the form
  `14_cal.py month [year]`
and does the following:
 - If the user doesn't specify any input, your program should
   print the calendar for the current month. The 'datetime'
   module may be helpful for this.
 - If the user specifies one argument, assume they passed in a
   month and render the calendar for that month of the current year.
 - If the user specifies two arguments, assume they passed in
   both the month and the year. Render the calendar for that
   month and year.
 - Otherwise, print a usage statement to the terminal indicating
   the format that your program expects arguments to be given.
   Then exit the program.
"""

import sys
import calendar
from datetime import datetime

# print(calendar.month(2019, 12))

# create calendar, starting on Mondays
c = calendar.TextCalendar(calendar.MONDAY)

# get user input integers split into list seperated by a space
user_input = input("Add month and year, ex 12 2019: ").split(' ')

today = datetime.today()
year = today.year
month = today.month


def str():
    if len(user_input) > 1:
      # if no numbers entered will return current month and year
        global month
        global year
        # specifing the value from user
        month = int(user_input[0])
        year = int(user_input[1])


str()

print(c.formatmonth(year, month))
