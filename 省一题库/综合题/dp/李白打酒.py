# from functools import lru_cache
# MOD = 10**9 + 7
#
# N, M = map(int, input().split())
# @lru_cache(maxsize=None)
# # s：已经遇到的店的次数
# # f：已经遇到的花的次数
# # w：当前酒壶里的酒量（单位：斗）
# def dfs(s, f, w):
#     if w < 0 or s > N or f > M-1:
#         return 0
#     if s == N and f == M-1:
#         return 1 if w == 1 else 0
#     res = 0
#     # 选择1：遇店
#     if s < N:
#         res += dfs(s+1, f, w*2)
#     # 选择2：遇花
#     if f < M-1 and w > 0:
#         res += dfs(s, f+1, w-1)
#     return res % MOD
# print(dfs(0, 0, 2))


# 满分ac代码，dp
MOD = 10 ** 9 + 7
n, m = map(int, input().split())
max_step = n + m
dp = [[[0] * 101 for _ in range(n + 1)] for __ in range(max_step + 1)]
dp[0][0][2] = 1
for i in range(1, max_step):
    for j in range(n + 1):
        for k in range(101):
            #遇花
            if k < 100:
                dp[i][j][k] = (dp[i][j][k] + dp[i - 1][j][k + 1]) % MOD
            #遇店
            if k % 2 == 0 and j > 0:
                dp[i][j][k] = (dp[i][j][k] + dp[i - 1][j - 1][k // 2]) % MOD
print(dp[max_step - 1][n][1] % MOD)





