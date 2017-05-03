from datetime import date, timedelta

date = date.today()
print("Today's date is {}".format((date)))
print("Thirty days before today was {}".format(date-timedelta(days=30)))
print("Thirty days later will be {}".format(date+timedelta(days=30)))
