import datetime

## Drops the microseconds
date = datetime.datetime.now().replace(microsecond=0)
print(date)

## Replaces the Hour to be '0'
x = datetime.datetime.now().replace(hour=0)
print(x)
