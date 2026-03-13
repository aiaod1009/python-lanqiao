n = 5
fa = list(range(n+1))
def find(x):   #找根节点
    if fa[x] == x: return x
    fa[x] = find(fa[x]) #路径压缩
    return fa[x]

def union(u,v):
    if find(u) != find(v):
        fa[find(v)] = find(u)

#优化，小树挂大树
# def union(self, x, y):
#     fx = self.find(x)
#     fy = self.find(y)
#     if fx == fy:
#         return
#     if self.size[fx] < self.size[fy]:
#         fx, fy = fy, fx
#     self.fa[fy] = fx
#     self.size[fx] += self.size[fy]


#菊花集
for x in range(1,n+1):
    fa[x] = find(x)
