import datetime

def week_number(date):
    x = date.split("-")
    week = (datetime.date(int(x[0]), int(x[1]), int(x[2])).isocalendar()[1])
    return week

date = input("Enter a date (format is 'Year-Month-Day'):\n>")
print(week_number(date))
