from datetime import datetime,timedelta
day1 = datetime(2000,1,1)
day2 = datetime(2024,4,13)
stroke = {
    '0': 13,
    '1': 1,
    '2': 2,
    '3': 3,
    '4': 5,
    '5': 4,
    '6': 4,
    '7': 2,
    '8': 2,
    '9': 2
}
count = 0
delta = timedelta(days=1)

curr = day1
while curr < day2:
    s = curr.strftime("%Y%m%d")
    tot = sum(stroke[c] for c in s)
    if tot > 50:
        count += 1
    curr += delta
print(count)