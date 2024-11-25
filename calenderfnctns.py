from datetime import datetime,date
import calendar
today= datetime.now()
print("Current date and time :",today)
yr=date.today()
print("Current year:",yr.year)
print("Month of the year:")
print(calendar.month(yr.year,yr.month))
print("Week Number of the year:",yr.strftime("%W"))
print("Weekday of the week:",yr.strftime("%A"))
print("Day of year:",yr.strftime("%j"))
print("Day of the Month:",yr.strftime("%d"))
print("Day of week:",yr.strftime("%w"))
