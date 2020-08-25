from datetime import datetime, time, date

current = datetime.now()
d = current.day
m = current.month
y = current.year
h = current.hour
m = current.minute
timestmp = current.timestamp()
print(d, m, y, h, m, timestmp)

formated = current.strftime("%m/%d/%Y, %H:%M:%S")
print(formated)

today = "5 December, 2019"
today_date = datetime.strptime(today, "%d %B, %Y")
print(today_date)

today = datetime(2020, 8, 25)
new_year_date = datetime(2021, 1, 1)
time_diff = new_year_date - current
print(time_diff)

new_time = datetime(1970, 1, 1)
print(today-new_time)
