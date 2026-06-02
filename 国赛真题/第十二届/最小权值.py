dp = [10**18] * (2022)
dp[0] = 0
dp[1] = 1
for i in range(2,2022):
    # 枚举j算dp[i]
    for j in range(i):
        r = i - 1 - j
        cost = 1 + 2*dp[j] + 3*dp[r] + j*j*r
        if cost < dp[i]:
            dp[i] = cost
print(dp[2021])