#暴力代码
n = int(input().strip())
a = list(map(int,input().split()))
ans = 0
for l in range(n):
    s,m = 0,1
    for r in range(l,n):
        s += a[r]
        s *= a[r]
        if m == s:
            ans += 1
        if m > 400000:
            break
print(ans)