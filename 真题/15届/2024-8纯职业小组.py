# 不会不会不会
#鸽巢原理 + 二分答案

def solve():
    n, k = map(int, input().split())
    ans = 0

    d = {}
    for i in range(n):
        a, b = map(int, input().split())
        d[a] = d.get(a, 0) + b

    l = []
    for i in d.values():
        ans += min(2, i)
        if i > 2: l.append(i - 2)

    for i in (3, 2, 1):
        for j in range(len(l)):
            if k == 1: break
            x = min(l[j] // i, k - 1)
            k, ans, l[j] = k - x, ans + x * i, l[j] - x * i

    print(ans + 1) if k == 1 and sum(l) != 0 else print(-1)


for _ in range(int(input())):
    solve()