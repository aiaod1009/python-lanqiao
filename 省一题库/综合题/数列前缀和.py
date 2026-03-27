import sys
input = lambda:sys.stdin.readline().strip()
t = int(input())
for _ in range(t):
    n,m,q = map(int,input().split())
    a = [[0] * (m + 1)]+[[0]+list(map(int,input().split())) for _ in range(n)]
    # a = [[0]*(m+1)]
    # for _ in range(n):
    #     row = list(map(int, input().split()))
    #     a.append([0] + row)

    s = [[0] * (m + 1) for _ in range(n + 1)]
    for i in range(1, n + 1):
        for j in range(1, m + 1):
            #遍历相加复杂度高，用公式很快
            #用已经算好的两块大矩形，拼出当前大矩形
            s[i][j] = s[i - 1][j] + s[i][j - 1] - s[i - 1][j - 1] + a[i][j]

    res = 0
    for _ in range(q):
        u, v, x, y = map(int, input().split())
        ans = s[x][y] + s[u - 1][v - 1] - s[u - 1][y] - s[x][v - 1]
        ans %= (1 << 64)  #就是2**64
        res ^= ans
    print(res)