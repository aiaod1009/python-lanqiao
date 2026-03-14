import os
import sys

# 请在此输入您的代码
s = input().strip()
n = len(s)
def val(c):
    return ord(c)-96
if n == 0:
    print(0)
elif n == 1:
    print(val(s[0]))
else:
    dp = [0] * n
    dp[0] = val(s[0])
    dp[1] = max(dp[0], val(s[1]))
    for i in range(2, n):
        dp[i] = max(dp[i-1], dp[i-2] + val(s[i]))
    print(dp[-1])
