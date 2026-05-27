n, m = map(int, input().split())
p = list(map(int, input().split()))
L = min(p)
R = max(p)
res = []
for i in range(1,n+1):
    res.append(str(max(i-L,R-i)))
print(' '.join(res))