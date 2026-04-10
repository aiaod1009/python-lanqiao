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

# 不用公式
n = int(input())
k = 1
while True:
    # 计算k种卡片能生成的不同无序两卡组合数（可重复）
    # 直接数：相同的有k种，不同的有k*(k-1)//2种，加起来就是总数
    total = k + k * (k - 1) // 2
    if total >= n:
        print(k)
        break
    k += 1