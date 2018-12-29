import calendar
day_name = ['MONDAY', 'TUESDAY', 'WEDNESDAY', 'THURSDAY', 'FRIDAY', 'SATURDAY', 'SUNDAY']
date = input().split()
year = int(date[2])
month = int(date[0])
day = int(date[1])

print(day_name[calendar.weekday(year,month,day)])
