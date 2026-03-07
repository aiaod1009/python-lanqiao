import os
import sys

# 请在此输入您的代码
# 读取输入并解析为6个整数
d1,p1,q1,d2,p2,q2 = map(int,sys.stdin.readline().split())
# print(d1,p1,q1,d2,p2,q2)

dirs = [(1,-1,0),(1,0,-1),(0,1,-1),(-1,1,0),(-1,0,-1),(0,-1,1)]

v1 = dirs[d1]
v2 = dirs[(d1+2)%6]
q_a = p1 * v1[0] + q1 * v2[0]
r_a = p1 * v1[1] + q1 * v2[1]
s_a = p1 * v1[2] + q1 * v2[2]

# 计算第二个点的轴向坐标
v3 = dirs[d2]
v4 = dirs[(d2+2)%6]
q_b = p2 * v3[0] + q2 * v4[0]
r_b = p2 * v3[1] + q2 * v4[1]
s_b = p2 * v3[2] + q2 * v4[2]

# 计算最短距离并输出
distance = max(abs(q_a - q_b), abs(r_a - r_b), abs(s_a - s_b))
print(distance)