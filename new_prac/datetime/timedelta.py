from datetime import date, timedelta, datetime

date = datetime.now().replace(microsecond=0)
print("Today's date is {}".format((date)))
print("12 Hours before now was {}".format(date-timedelta(hours=12)))
print("10 Hours later will be {}".format(date+timedelta(hours=10)))
