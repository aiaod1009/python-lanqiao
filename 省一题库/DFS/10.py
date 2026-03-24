def dfs(a,p,last):
    if a == 0:
        return 1
    if p == 0:
        return 0
    ans = 0
    for i in range(0,min(a,p) + 1):
        ans += dfs(a-i,p-1,i)
    return ans

t = int(input())
for _ in range(t):
    m,n = map(int,input().split())
    print(dfs(m,n,m))




# 记忆化搜索版本，最直观
from functools import lru_cache
@lru_cache(maxsize=None)
def dp(apple, plate):
    if apple == 0:
        return 1
    if plate == 0:
        return 0
    if plate > apple:
        return dp(apple, apple)
    # 核心公式：不放第 plate 个 + 每个盘子先放 1 个
    return dp(apple, plate - 1) + dp(apple - plate, plate)


t = int(input())
for _ in range(t):
    m, n = map(int, input().split())
    print(dp(m, n))