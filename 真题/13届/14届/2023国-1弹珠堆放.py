import os
import sys

# 请在此输入您的代码

total = 0  # 总珠子
layer = 0  # 当前层
line = 0  # 当前这一行的和
max = 20230610
while True:
    layer += 1
    line += layer  # 只做加法：1+2+3+4+...
    total += line  # 再把这一行加进总数

    if total > max:
        print(layer - 1)
        break
