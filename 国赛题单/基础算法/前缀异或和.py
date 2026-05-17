import sys
input = lambda:sys.stdin.readline().strip()
n,m = map(int,input().split())
a = [0]+list(map(int,input().split()))
pre = [0] * (n+1)
for i in range(1,n+1):
    pre[i] = pre[i-1]^a[i]

for _ in range(m):
    l,r = map(int,input().split())
    print(pre[r]^pre[l-1])


