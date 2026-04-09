#可以暴力
n = int(input())
a = input().split()
dp = [0] * 10
for s in a:
    h = int(s[0])
    t = int(s[-1])
    # dp[t] = 原来就有的、以t结尾的最长长度
    # dp[h] + 1 = 把当前数字接上去后，新的长度
    dp[t] = max(dp[t],dp[h]+1)
print(n-max(dp))