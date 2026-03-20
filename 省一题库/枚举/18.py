d = [0,31,28,31,30,31,30,31,31,30,31,30,31]
cnt = 0
for y in range(2000,2000000):
    if (y % 4 == 0 and y % 100 != 0) or y % 400 == 0:
        d[2] = 29
    else:
        d[2] = 28
    for m in range(1,13):
        for x in range(1,d[m] + 1):
            if y % m == 0 and y % x == 0:
                cnt += 1
print(cnt+1)