import os
import sys

# 请在此输入您的代码
n = int(sys.stdin.readline())
h = list(map(int,sys.stdin.readline().split()))
Max = 1
for d in range(1,n):
  for i in range(n):
    tree = [h[i] for i in range(i,n,d)]
    cnt = 1
    for i in range(1,len(tree)):
      if tree[i] > tree[i-1]:
        cnt += 1
      else:
        break
    Max = max(Max,cnt)
print(Max)