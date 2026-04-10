import os
import sys
import math

# 请在此输入您的代码
n = int(input())

# k = math.ceil((math.sqrt(8*n+1)-1) / 2)
# print(k)
k = 1
while True:
  c = k * (k + 1) // 2
  if c >= n:
    break
  k += 1
print(k)

n = int(input())
k = 1
while k * (k + 1) // 2 < n:
    k += 1
print(k)