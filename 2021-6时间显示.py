import os
import sys
# 请在此输入您的代码

# 法一
# ms = int(input())
# t = ms // 1000
# d = t % (24 * 3600)

# h = d // 3600
# r = d % 3600
# m = r // 60
# s = r % 60

# print(f"{h:02d}:{m:02d}:{s:02d}")

# 法二
from datetime import datetime,timedelta

ms = int(input())

epoch = datetime(1970,1,1)
time = epoch + timedelta(milliseconds=ms)

t = time.strftime("%H:%M:%S")

print(t)