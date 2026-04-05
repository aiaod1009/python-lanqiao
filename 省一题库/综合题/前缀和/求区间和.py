import sys
input = lambda:sys.stdin.readline().strip()
n = int(input())
a = [0]+list(map(int,input().split()))
m = int(input())
# for _ in range(m):
#     l,r = map(int,input().split())
#     ans = 0
#     for i in range(l,r+1):
#         ans += a[i]
#     print(ans)


#前缀和做法
s = [0] * (n+1)
for i in range(1,n+1):
    s[i] = s[i-1] + a[i]
for _ in range(m):
    l,r = map(int,input().split())
    print(s[r] - s[l-1])