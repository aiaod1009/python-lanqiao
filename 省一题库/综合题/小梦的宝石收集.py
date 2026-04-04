t = int(input().strip())
for _ in range(t):
    n, k = map(int, input().split())
    a = list(map(int, input().split()))
    a.sort()
    a = [0] + a
    ans = 10 ** 18
    for i in range(1, n + 1):
        if i - 1 > k:
            break
        l, r = i, n
        while l < r:
            mid = (l + r) // 2
            # 核心操作次数公式，和AC代码完全一致
            cost = (i-1) + (n-mid) + min(i-1, n-mid)
            if cost <= k:
                r = mid
            else:
                l = mid + 1
        ans = min(ans, a[l] - a[i])
    print(ans)