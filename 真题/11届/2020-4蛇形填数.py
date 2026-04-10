i_target = 20
j_target = 20

# 1. 计算所在斜行k
k = i_target + j_target - 1  # 39

# 2. 计算前k-1斜行的总数字数（1+2+...+38）
sum_before = (k - 1) * k // 2  # 38×39//2=741

# 3. 计算目标数（奇数斜行，偏移量=k - i_target）
result = sum_before + (k - i_target + 1)  # 741 + (39-20+1)=761

print(result)  # 直接输出761


import os
import sys

# 数学题目啦，直接找规律，中间斜线上面的是我们目标的数字，1、5、13、25......
#很明显是递加上(n-1)*4+上一个数字嘛
sum=1                #这里是因为第一个数字是1呀
for i in range(1,21):
  sum=(i-1)*4+sum
print(sum)