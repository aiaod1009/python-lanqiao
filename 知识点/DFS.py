# def环，也可以用并查集
n = int(input())
g = [0] + list(map(int, input().split()))
res = 0
d = {}

def dfs(u, idx):
    global res
    # 改成新手友好版，逻辑完全不变
    if u in d:  # 替换了原来的 d.get(u) is not None
        res = max(res, idx - d[u])
        return
    d[u] = idx
    dfs(g[u], idx + 1)

for u in range(1, n + 1):
    dfs(u, 1)

print(res)