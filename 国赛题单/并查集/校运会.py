import sys
input = lambda:sys.stdin.readline().strip()
n,m = map(int,input().split())
name = {}
for i in range(1,n+1):
    name[input()] = i
fa = list(range(n+1))
def find(x):
    if fa[x] != x:
        fa[x] = find(fa[x])
    return fa[x]
for _ in range(m):
    u,v = input().split()
    fa[find(name[u])] = find(name[v])
k = int(input())
for _ in range(k):
    x,y = input().split()
    if find(name[x]) == find(name[y]):
        print("Yes")
    else:
        print("No")