import sys
input = lambda:sys.stdin.readline().strip()
n = int(input())
a = [0]+list(map(int,input().split()))
m = int(input())
pre = [0] * (n+1)
for i in range(1,n+1):
    pre[i] = pre[i-1] + a[i]
for _ in range(m):
    l,r = map(int,input().split())
    print(pre[r] - pre[l-1])