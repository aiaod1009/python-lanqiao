import os
import sys

# 请在此输入您的代码

L = int(sys.stdin.readline())
count = 0
for xa in range(1, L + 1):
    for ya in range(1, L + 1):
      for yb in range(1, L // ya + 1):
        max_xb = (L - ya * yb) // xa
        if max_xb >= 1:
          count += max_xb

print(count)