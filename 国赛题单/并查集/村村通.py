import sys
input = lambda:sys.stdin.readline().strip()
while True:
    line = input()
    if not line:
        break
    parts = list(map(int, line.split()))
    n = parts[0]
    if n == 0:
        break
    m = parts[1]
    if n == 0:
        break
    fa = list(range(n+1))
    def find(x):
        if fa[x] != x:
            fa[x] = find(fa[x])
        return fa[x]
    def union(u, v):
        ru, rv = find(u), find(v)  # 先存下来
        if ru != rv:
            fa[ru] = rv  # 干净利落
    for _ in range(m):
        u,v = map(int,input().split())
        union(u,v)
    crc = 0
    for i in range(1,n+1):
        if fa[i] == i:
            crc += 1
    print(crc-1)

