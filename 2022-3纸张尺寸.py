import os
import sys

# 请在此输入您的代码
arr =[[] for _ in range(9)]
arr[0] = [1189,841]
for i in range(1,9):
  if arr[i-1][0] > arr[i-1][1]:
    l = arr[i-1][0] //2
    w = arr[i-1][1]
  else:
    w = arr[i-1][0]
    l = arr[i-1][1] // 2
  arr[i] = [l,w]

s = int(input()[1:])
print(arr[s][0])
print(arr[s][1])
