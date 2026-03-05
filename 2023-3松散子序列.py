import os
import sys

# 请在此输入您的代码
s = input().strip()
n = len(s)
if n == 0:
    print(0)
elif n == 1:
    print(ord(s[0]) - ord('a') + 1)
else:
    dp = [0] * n
    dp[0] = ord(s[0]) - ord('a') + 1
    dp[1] = max(dp[0], ord(s[1]) - ord('a') + 1)
    for i in range(2, n):
        val = ord(s[i]) - ord('a') + 1
        dp[i] = max(dp[i-1], dp[i-2] + val)
    print(dp[-1])
