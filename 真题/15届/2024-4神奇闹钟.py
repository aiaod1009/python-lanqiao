import sys
from datetime import datetime, timedelta
epoch = datetime(1970, 1, 1, 0, 0, 0)

T = int(input())

for _ in range(T):
  line = sys.stdin.readline().strip()
  parts = line.split()  # 拆成 ["2016-09-07", "18:24:33", "10"]
  time_str = " ".join(parts[:2])  # 合并前两项为完整时间字符串
  x = int(parts[2])

  ctime = datetime.strptime(time_str,"%Y-%m-%d %H:%M:%S")

  total_s = (ctime - epoch).total_seconds()

  interval = x * 60

  last = total_s - (total_s % interval)

  last_time = epoch + timedelta(seconds=last)

  print(last_time.strftime("%Y-%m-%d %H:%M:%S"))

# import sys
# from datetime import datetime,timedelta
# T = int(input())
#
# d0 = datetime(1970,1,1,0,0,0)
#
# for _ in range(T):
#     s = sys.stdin.readline().strip()
#     part = s.split()
#     t = ' '.join(part[:2])
#     x = int(part[2])
#     t1 = datetime.strptime(t,"%Y-%m-%d %H:%M:%S")
#     total = (t1 - d0).total_seconds()
#     x *= 60
#     last = total - (total % x)
#
#     ans = d0 + timedelta(seconds=last)
#     print(ans.strftime("%Y-%m-%d %H:%M:%S"))