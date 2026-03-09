from datetime import date,timedelta

s = date(2000,1,1)
e = date(2020,10,1)
total = 0

d = s
while d <= e:
    total += 2 if (d.weekday()==0 or d.day == 1) else 1
    d += timedelta(days=1)

print(total)
