n,m = map(int,input().split())
p = list(map(int,input().split()))
l = min(p)
r = max(p)
res = []
for i in range(1,n+1):
    res.append(str(max(i-l,r-i)))
print(' '.join(res))