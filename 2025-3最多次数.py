import os
import sys

w, h, v = map(int, sys.stdin.readline().split())
# 请在此输入您的代码
for i in range(h):
    print('Q' * w)

for i in range(w):
    print('Q' * (v + w))
