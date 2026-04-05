n = int(input())
a = list(map(int,input().split()))
dp = [0] * 32  # 初始化32个二进制位的最长长度，默认0
ans = 0
for n in a:
    best = 1
    # 🔹 第一步：计算当前数能组成的最长长度best
    for i in range(32):
        # 按位与 & 不为 0 → 两个数至少有一个共同的二进制位是 1
        if n & (1 << i):  #造一个 “只有第 i 位是 1，其他全是 0” 的面具
            best = max(best,dp[i] + 1)
    for i in range(32):
        if n & (1 << i):
            dp[i] = max(dp[i],best)
    ans = max(ans,best)
print(ans)