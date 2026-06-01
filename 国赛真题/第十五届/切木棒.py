n,m = map(int,input().split())
L = list(map(int,input().split()))
l = 1
r = max(L)
ans = r
while l <= r:
    mid = (l+r) // 2
    total = 0
    for le in L:
        if le > mid:
            total += (le-1) // mid
    if total <= m:
        ans = mid
        r = mid - 1
    else:
        l = mid + 1
print(ans)
