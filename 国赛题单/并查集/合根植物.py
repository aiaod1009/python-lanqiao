import sys
input = lambda:sys.stdin.readline().strip()
m,n = map(int,input().split())
k = int(input())
fa = list(range(m*n+1))
def find(x):
    if fa[x] != x:
        fa[x] = find(fa[x])
    return fa[x]

for _ in range(k):
    u,v = map(int,input().split())
    fa[find(u)] = find(v)
ans = 0
for i in range(1,n*m+1):
    if fa[i] == i:
        ans += 1
print(ans)

