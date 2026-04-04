import math
n,m = map(int,input().split())
a = [0]+list(map(int,input().split()))
def ok(l):
    cnt = 0
    for i in range(1,n+1):
        dis = a[i]-a[i-1]
        # cnt += math.ceil(dis/l)-1
        cnt += (dis + l - 1) // l - 1
    return cnt <= m+1
l = 1
r = a[-1]
while l < r:
    mid = (l+r) // 2
    if ok(mid):
        r = mid
    else:
        l = mid + 1
print(l)