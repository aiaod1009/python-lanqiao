from functools import lru_cache
MOD = 10**9 + 7

N, M = map(int, input().split())
@lru_cache(maxsize=None)
# s：已经遇到的店的次数
# f：已经遇到的花的次数
# w：当前酒壶里的酒量（单位：斗）
def dfs(s, f, w):
    if w < 0 or s > N or f > M-1:
        return 0
    if s == N and f == M-1:
        return 1 if w == 1 else 0
    res = 0
    # 选择1：遇店
    if s < N:
        res += dfs(s+1, f, w*2)
    # 选择2：遇花
    if f < M-1 and w > 0:
        res += dfs(s, f+1, w-1)
    return res % MOD
print(dfs(0, 0, 2))