def leap_year(year):
    if (year % 4 == 0) or (year % 100 == 0) or (year % 400 == 0):
        return "{} IS a Leap Year!".format(year)
    else:
        return "{} is NOT a Leap Year!".format(year)

year = int(input("Enter a year to see if it is a leap year:\n>"))
print(leap_year(year))
