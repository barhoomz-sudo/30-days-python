from datetime import datetime, date

# Get the current day, month, year, hour, minute and timestamp from datetime module
    # now = datetime.now()
    # day = now.day
    # month = now.month
    # year = now.year
    # hour = now.hour
    # minute = now.minute
    # timestamp = now.timestamp()
# Format the current date using this format: "%m/%d/%Y, %H:%M:%S")
#   print(now.strftime("%m/%d/%Y, %H:%M:%S"))
# Today is 5 December, 2019. Change this time string to time.
    # print(now.strptime("5 December, 2019", "%d %B, %Y"))
# Calculate the time difference between now and new year.
    # d = date(year, month, day)
    # today = d.today()
    # new_year = date(2027, 1, 1)
    # time_left_for_new_year = new_year - today
    # print(time_left_for_new_year)
# Calculate the time difference between 1 January 1970 and now.
    # ninty_seventy = date(1970, 1, 1)
    # print(today - ninty_seventy)