#并查集
class UnionFind:
    def __init__(self, n):
        self.fa = list(range(n + 1))  # 初始化父节点
        self.size = [1] * (n + 1)    # 初始化连通块大小

    def find(self, x):
        if self.fa[x] == x:
            return x
        self.fa[x] = self.find(self.fa[x])  # 路径压缩
        return self.fa[x]

    def union(self, x, y):
        fx = self.find(x)
        fy = self.find(y)
        if fx == fy:
            return
        if self.size[fx] < self.size[fy]:
            fx, fy = fy, fx
        self.fa[fy] = fx
        self.size[fx] += self.size[fy]

def cal(x):
    return x * (x - 1) // 2  # 组合数：x个节点的两两对数

# 主程序（核心逻辑不变）
n, m, l, r = map(int, input().split())
uf1 = UnionFind(n)  # 费用 ≤ R 的边
uf2 = UnionFind(n)  # 费用 < L 的边

for _ in range(m):
    u, v, w = map(int, input().split())
    if w <= r:
        uf1.union(u, v)
    if w < l:
        uf2.union(u, v)

ans = 0
for i in range(1, n + 1):
    if i == uf1.find(i):
        ans += cal(uf1.size[i])
    if i == uf2.find(i):
        ans -= cal(uf2.size[i])

print(ans)