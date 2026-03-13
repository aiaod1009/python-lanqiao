n = 5
fa = list(range(n+1))
def find(x):   #找根节点
    if fa[x] == x: return x
    fa[x] = find(fa[x]) #路径压缩
    return fa[x]

def union(u,v):
    if find(u) != find(v):
        fa[find(v)] = find(u)


#菊花集
for x in range(1,n+1):
    fa[x] = find(x)
