import os
import sys
from collections import Counter
# 请在此输入您的代码

s=sys.stdin.readline().strip()

count = Counter(s)

for c in count:
  if count[c] % 2 != 0:
    print("NO")
    exit()

print("YES")