from datetime import datetime, date

# print(dir(datetime))

# datetime
now = datetime.now()
# print(now)
day = now.day
month = now.month
year = now.year
hour = now.hour
minute = now.minute
second = now.second
timestamp = now.timestamp()

# print(year, month, day, hour, minute, second, timestamp)

# t = now.strftime("%H:%M:%S")
# print(t)
# d = now.strftime("%d/%m/%Y")
# print(d)

# string to time using strptime()
# d_str = '13 November, 2002'
# d_obj = datetime.strptime(d_str, "%d %B, %Y")
# print(d_obj)

d = date(2002, 11, 13)
# print(d.today())

today = d.today()
new_year = date(2027, 1, 1)

time_left_for_new_year = new_year - today
print(time_left_for_new_year)