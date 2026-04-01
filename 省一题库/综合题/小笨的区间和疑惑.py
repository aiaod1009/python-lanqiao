n = int(input())
a = list(map(int,input().split()))

l = [0] * n
l[0] = a[0]
for i in range(1,n):
    l[i] = max(a[i],l[i-1]+a[i])

r = [0] * n
r[-1] = a[-1]
         # 倒数第二个元素
for i in range(n-2,-1,-1):
    r[i] = max(a[i],r[i+1]+a[i])

ans = [l[i] + r[i] -a[i] for i in range(n)]
print(' '.join(map(str,ans)))