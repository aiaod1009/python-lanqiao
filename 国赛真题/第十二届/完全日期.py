import datetime
import math
s = datetime.date(2001,1,1)
e = datetime.date(2021,12,31)
cnt = 0
cur = s
while cur <= e:
    s = str(cur).replace('-','')
    total = sum(int(c) for c in s)
    if int(total**0.5) == total**0.5:
        cnt += 1
    # k = int(math.isqrt(total))
    # if k * k == total:
    #     cnt += 1
    cur += datetime.timedelta(days=1)
print(cnt)

# str(cur)默认格式YYYY-MM-DD，所以replace('-','')等价年+月+日拼接