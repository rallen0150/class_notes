import datetime
import time

print("The current date and time is {}".format(datetime.datetime.now()))
print("The current year is {}".format(datetime.date.today().strftime("%Y")))
print("The current month is {}".format(datetime.date.today().strftime("%B")))
print("Today is in the {} week of the year".format(datetime.date.today().strftime("%U")))
print("Today is the {} day in the week".format(datetime.date.today().strftime("%w")))
print("Today is in the {} day in the year".format(datetime.date.today().strftime("%j")))
print("Today is in the {} day in the month of {}".format(datetime.date.today().strftime("%d"), datetime.date.today().strftime("%B")))
print("Today is {}".format(datetime.date.today().strftime("%A"))) # The day of the week
