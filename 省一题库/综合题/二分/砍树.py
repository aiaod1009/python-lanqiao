n,m = map(int,input().split())
a = list(map(int,input().split()))
l = 0
r = max(a)
ans = 0
while l <= r:
    mid = (l+r) // 2  #树的高度
    tot = 0
    for x in a:
        if x > mid:
            tot += x - mid
            if tot >= m:
                break
    if tot >= m:
        ans = mid
        l = mid + 1 #尝试找更高的合法高度
    else:
        r = mid - 1
print(ans)
