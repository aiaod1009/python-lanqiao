import sys
input = lambda:sys.stdin.readline().strip()
n= int(input().strip())
a = [0]+list(map(int,input().split()))
fa = list(range(n+1))
sz = [1] * (n+1)# 一开始，每个人自己就是一个圈子，人数为 1
def find(x):
    if fa[x] != x:
        fa[x] = find(fa[x])
    return fa[x]
def union(u,v):
    ru,rv = find(u),find(v)
    if ru != rv:
        fa[ru] = rv
        sz[rv] += sz[ru] #因为我们在合并时，必须要更新整个圈子的人数（sz）。
for i in range(1,n + 1):
    union(i,a[i])
if sz[find(1)] == n:
    print(n)
else:
    max_ans = 0
    for j in range(1,n):
        rj1,rj2 = find(j),find(j+1)
        if rj1 != rj2:
            max_ans = max(max_ans,sz[rj1] + sz[rj2])
    if max_ans == 0:
        max_ans = max(sz)
    print(max_ans)