class UnionFind:
    def __init__(self, n):
        self.fa = list(range(n+1))
        self.size = [1] * n

    def find(self, x):
        if x != self.fa[x]:
            rx = self.find(self.fa[x])
            self.fa[x] = rx
            return rx
        return x

    def union(self, x, y):
        rx, ry = self.find(x), self.find(y)
        if rx == ry:
            return
        self.fa[ry] = rx
        self.size[rx] += self.size[ry]

def cal(x):
    return x * (x - 1) // 2


n, m, l, r = map(int, input().split())
uf1 = UnionFind(n + 1)
uf2 = UnionFind(n + 1)

for i in range(m):
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