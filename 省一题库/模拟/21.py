import sys
from datetime import datetime,timedelta
ep = datetime(1970,1,1,0,0,0)
T = int(input())
for i in range(T):
    s = sys.stdin.readline().strip().split()
    t = ' '.join(s[:2])
    d = datetime.strptime(t,"%Y-%m-%d %H:%M:%S")
    x = int(s[2]) *60
    total = (d-ep).total_seconds()
    total -= (total % x)
    last = ep+timedelta(seconds=total)
    print(last.strftime("%Y-%m-%d %H:%M:%S"))

