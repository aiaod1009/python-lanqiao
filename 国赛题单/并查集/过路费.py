import sys
input = lambda:sys.stdin.readline().strip()
n,m,l,r = map(int,input().split())
e = []
for _ in range(m):
    u,v,w = map(int,input().split())
    e.append((w,u,v))
e.sort()  #从低到高排好序
fa = list(range(n+1))
sz = [1] * (n+1)
def find(x):
    if fa[x] != x:
        fa[x] = find(fa[x])
    return fa[x]
ans = 0
for w,u,v in e :
    if w > r:
        break
    ru, rv = find(u), find(v)
    if ru != rv:
        if l <= w <= r:
            ans += sz[ru] * sz[rv]
        fa[ru] = rv
        sz[rv] += sz[ru]
print(ans)