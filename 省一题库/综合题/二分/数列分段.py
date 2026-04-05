n,m = map(int,input().split())
a = list(map(int,input().split()))
l, r = max(a), sum(a)
ans = r

while l <= r:
    mid = (l + r) // 2
    cnt, s = 1, 0  #s = 当前这一段的总和  cnt = 现在一共分了多少段
    for x in a:
        if s + x > mid:
            cnt += 1
            s = x
        else:
            s += x
    if cnt <= m:
        ans = mid
        r = mid - 1  # 可行
    else:
        l = mid + 1

print(ans)