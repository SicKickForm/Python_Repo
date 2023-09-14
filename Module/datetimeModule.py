import datetime as Date

# Datetime module methods
# Datetime module includes various methods to show date and time
print("date")
print(Date.date(2003, 1, 17))
print("time")
print(Date.time(19, 37))
print("datetime")
print(Date.datetime(2003, 1, 17, 19, 37))
print("now")
print(Date.datetime.now())
print(Date.datetime.now().year)
print(Date.datetime.now().month)
print(Date.datetime.now().day)
print(Date.datetime.now().weekday())
print(Date.datetime.now().hour)
print(Date.datetime.now().minute)
print(Date.datetime.now().second)
print(Date.datetime.now().microsecond)
# Use strftime command to format date objects into readable strings
# strftime methods
print('strftime')
# Date and time methods
print('Date and time')
print(Date.datetime.now().strftime('%c'))
print(Date.datetime.now().strftime('%x'))
print(Date.datetime.now().strftime('%X'))
# Year methods
print('Year')
print(Date.datetime.now().strftime('%C'))
print(Date.datetime.now().strftime('%G'))
print(Date.datetime.now().strftime('%Y'))
print(Date.datetime.now().strftime('%y'))
# Month methods
print('Month')
print(Date.datetime.now().strftime('%B'))
print(Date.datetime.now().strftime('%b'))
print(Date.datetime.now().strftime('%m'))
# Week methods
print('Week')
print(Date.datetime.now().strftime('%U'))
print(Date.datetime.now().strftime('%W'))
print(Date.datetime.now().strftime('%V'))
# Day methods
print('Day')
print(Date.datetime.now().strftime('%A'))
print(Date.datetime.now().strftime('%a'))
print(Date.datetime.now().strftime('%j'))
print(Date.datetime.now().strftime('%d'))
print(Date.datetime.now().strftime('%w'))
print(Date.datetime.now().strftime('%u'))
# Hour methods
print('Hour')
print(Date.datetime.now().strftime('%H'))
print(Date.datetime.now().strftime('%I'))
print(Date.datetime.now().strftime('%p'))
# Minute method
print('Minute')
print(Date.datetime.now().strftime('%M'))
# Second method
print('Second')
print(Date.datetime.now().strftime('%S'))
# Micro second method
print('Micro second')
print(Date.datetime.now().strftime('%f'))
print(Date.datetime.now().strftime('%%'))
print("timedelta")
print(Date.datetime(2022, 7, 21) - Date.timedelta(18*365))
print(Date.datetime(2003, 1, 17) + Date.timedelta(days=18*365))
print(Date.timedelta(hours=60))
print("total_seconds")
print(Date.timedelta(minutes=1824).total_seconds())

