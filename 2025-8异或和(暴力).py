import sys

n = int(input())
a = list(map(int,sys.stdin().readline().split()))
a.sort()
pre = [0] * (n + 1)
ans = 0
for i in range(n):
    pre[i+1] = pre[i] + a[i]
    ans += a[i] * i - pre[i]
print(ans)
