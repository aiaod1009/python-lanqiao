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

s = input().strip()
n = len(s)
max_sum = 0
# 暴力DFS：枚举选/不选
def dfs(pos, last, current):
    global max_sum
    # 走到最后，更新最大值
    if pos == n:
        max_sum = max(max_sum, current)
        return

    # 不选当前字符
    dfs(pos + 1, last, current)

    # 选当前字符（必须满足：和上一个位置差 >=2）
    if last == -1 or pos - last >= 2:
        val = ord(s[pos]) - ord('a') + 1
        dfs(pos + 1, pos, current + val)


dfs(0, -1, 0)
print(max_sum)