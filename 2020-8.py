n = int(input())

dp = []
for _ in range(n):
    row = list(map(int,input().split()))
    dp.append(row)

for i in range(1,n):
    for j in range(i + 1):
        if j == 0:
            dp[i][j] += dp[i-1][j]
        elif j == i:
            dp[i][j] += dp[i-1][j-1]
        else:
            dp[i][j] += max(dp[i-1][j-1],dp[i-1][j])

last = dp[-1]
if n % 2 == 1:
    res = last[n // 2]
else:
    res = max(last[n // 2 - 1],last[n // 2])

print(res)
