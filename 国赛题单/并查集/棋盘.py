import sys
input = lambda:sys.stdin.readline().strip()
n,m = map(int,input().split())
fa = list(range((n+1)*(n+1)))
grid = [[-1]*(n+1) for _ in range(n+1)]
def find(x):
    if fa[x] != x:
        fa[x] = find(fa[x])
    return fa[x]
cnt = 0
for _ in range(m):
    c,x,y = map(int,input().split())
    grid[x][y] = c  # 落子染色
    cnt += 1
    cid = x * (n + 1) + y
    for dx,dy in [(-1,0),(1,0),(0,-1),(01)]:
        nx,ny = x + dx,y + dy
        if 1 <= nx <= n and 1 <= ny <= n:
            if grid[nx][ny] == c:
                nid = nx * (n + 1) + ny
                rc = find(cid)
                rn = find(nid)
                if rc != rn:
                    fa[rc] = rn
                    cnt -= 1
    print(cnt)



