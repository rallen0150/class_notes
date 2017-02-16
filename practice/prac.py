import sys
import datetime

print(sys.version)
print(sys.version_info)

time = datetime.datetime.now()
print(time.strftime("%m-%d-%Y %H:%M"))
