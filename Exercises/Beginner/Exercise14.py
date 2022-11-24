#datetime.date(year, month, day) Returns date object with same year, month and day.

from datetime import date

t1=date(2019, 10, 1)
t2=date(2019, 10, 30)
delta = t2-t1
print(delta)
# Or below to not receive time
print(delta.days)


