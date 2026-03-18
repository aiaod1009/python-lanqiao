from datetime import datetime
import sys

with open("1.in", "r", encoding="utf-8") as f:
    lines = [l.strip() for l in f]

tl = [datetime.strptime(l,"%Y-%m-%d %H:%M:%S") for l in lines]
tl.sort()

tot = 0
for i in range(0,len(tl),2):
    t = tl[i+1]-tl[i]
    tot += t.total_seconds()   #浮点数
print(int(tot))