import os
import sys

# 请在此输入您的代码

data = sys.stdin.read().split()
n = int(data[0])
parts = data[1:n+1]
# 初始化：dp0/dp1 = (最后字符, 总长度)
f = parts[0]
dp0 = (f[1], 2)  # 不翻转
dp1 = (f[0], 2)  # 翻转

# 遍历后续工件
for p in parts[1:]:
    # 当前工件的两种状态首尾字符
    c0, c1 = (p[0], p[1]), (p[1], p[0])
    # 计算四种转移成本
    cost00 = 1 if dp0[0]==c0[0] else 2
    cost01 = 1 if dp1[0]==c0[0] else 2
    cost10 = 1 if dp0[0]==c1[0] else 2
    cost11 = 1 if dp1[0]==c1[0] else 2
    # 更新状态：选成本最小的转移
    new_dp0 = (c0[1], min(dp0[1]+cost00, dp1[1]+cost01))
    new_dp1 = (c1[1], min(dp0[1]+cost10, dp1[1]+cost11))
    dp0, dp1 = new_dp0, new_dp1

print(min(dp0[1], dp1[1]))