import calendar
# Prints the days in a specific month from a specific year
print(calendar.monthrange(2016, 4), calendar.monthrange(2016, 2))

# Prints the Calendar
print(calendar.calendar(2016))

# Prints the Calendar with the start as a 'SUNDAY'
x = calendar.TextCalendar(calendar.SUNDAY)
x.prmonth(2017, 4)

# User input to show the calendar of a specific month and year
def find_date(year, month):
    return calendar.month(year, month)

year = int(input("\nEnter a Year: "))
month = int(input("Enter a Month (Number): "))
print("\n",find_date(year, month))

# Print all Calender Month by Name
for name in calendar.month_name:
    print(name)
print('\n')
# Print the Day by Name (Monday, Tuesday, ...)
for day in calendar.day_name:
    print(day)

# Find the first Friday of every month in 2025
print("\nThe first FRIDAY of every month in the year 2025:")
for month in range(1, 13):
    cal = calendar.monthcalendar(2025, month)

    week1 = cal[0]
    week2 = cal[1]

    if week1[calendar.FRIDAY] != 0:
        day = week1[calendar.FRIDAY]
    else:
        day = week2[calendar.FRIDAY]
    print("{}-{}".format(calendar.month_name[month], day))
