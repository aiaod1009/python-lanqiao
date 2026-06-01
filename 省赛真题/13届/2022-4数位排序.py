import os
import sys

# 请在此输入您的代码

n = int(input())
m = int(input())
nums = list(range(1, n+1))

def sort_key(x):
  s = sum(int(c) for c in str(x))
  return s,x

nums_s = sorted(nums, key=sort_key)
print(nums_s[m-1])