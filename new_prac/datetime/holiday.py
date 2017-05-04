from datetime import date
import holidays
import calendar

print(date(2014, 1, 1) in holidays.US())

print("\nList of US Holidays in 2017:")
for date, name in sorted(holidays.US(state='SC', years=2017).items()):
    print(date, name)

print("\nList of Canadian Holidays in 2017:")
for date, name in sorted(holidays.Canada(years=2017).items()):
    print(date, name)


us_holiday = holidays.UnitedStates()
canadian_holiday = holidays.Canada()


date = input("\nEnter a date to see if that date is a Holiday (format: 'Year-Month-Day'):\n>")
if us_holiday.get(date):
    print(us_holiday.get(date))
    date = date.split("-")
    year = date[0]
    month = date[1]
    print(calendar.month(int(year), int(month)))
elif canadian_holiday.get(date):
    print(canadian_holiday.get(date))
    date = date.split("-")
    year = date[0]
    month = date[1]
    print(calendar.month(int(year), int(month)))
else:
    print("That isn't a US or Canadian Holiday!")
