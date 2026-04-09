n = int(input())
a = list(map(int,input().split()))
p = [0]*(n+1)
ans = float('inf')
for i in range(n):
    p[i+1] = p[i]+a[i]
for l1 in range(n):
    for r1 in range(l1,n):
        t1 = p[r1+1]-p[l1]
        for l2 in range(r1+1,n):
            for r2 in range(l2,n):
                t2 = p[r2+1]-p[l2]
                ans = min(ans,abs(t1-t2))
print(ans)