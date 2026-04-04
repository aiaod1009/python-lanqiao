t = int(input().strip())
for _ in range(t):
    n, k = map(int, input().split())
    a = list(map(int, input().split()))
    a.sort()
    a = [0] + a
    ans = 10 ** 18
    for i in range(1, n + 1):
        # i是左端点
        if i - 1 > k:
            break
        l, r = i, n
        while l < r:
            mid = (l + r) // 2
            # 计算保留[i, mid]区间需要的操作次数
            cost = (i-1) + (n-mid) + min(i-1, n-mid)
            if cost <= k:
                r = mid  # 可行，尝试更小的r（缩小极差）
            else:
                l = mid + 1 # 不可行，需要更大的r
            # 到最后l==r
        ans = min(ans, a[l] - a[i])
    print(ans)