import sys
input = lambda:sys.stdin.readline().strip()
n = int(input())
g = [list(map(int, input().split())) for _ in range(n)]
dirs = [(-1, 0), (1, 0), (0, -1), (0, 1)]
def dfs(x, y):   #（核心：标记圈外 0）
    g[x][y] = 3
    for dx, dy in dirs:
        nx = x + dx
        ny = y + dy
        # 新坐标在矩阵内，且是未访问的 0
        if 0 <= nx < n and 0 <= ny < n and g[nx][ny] == 0:
            dfs(nx, ny)
# 1. 从边界 0 开始 DFS，标记所有圈外 0 为 3
for i in range(n):
    for j in range(n):
        if (i == 0 or i == n-1 or j == 0 or j == n-1) and g[i][j] == 0:
            dfs(i, j)
# 2. 替换数字：圈内 0 → 2，圈外 3 → 0
# for i in range(n):
#     for j in range(n):
#         if g[i][j] == 0:
#             g[i][j] = 2
#         elif g[i][j] == 3:
#             g[i][j] = 0
# for row in g:
#     print(' '.join(map(str, row)))
for row in g:
    print(' '.join('2' if x == 0 else '0' if x == 3 else str(x) for x in row))

#如果加虚拟边界，就不需要遍历边界每个点了，但是输入输出更麻烦
import sys
input = lambda: sys.stdin.readline().strip()
n = int(input())
g = [[0]*(n+2) for _ in range(n+2)]
for i in range(1, n+1):
    row = list(map(int, input().split()))
    for j in range(1, n+1):
        g[i][j] = row[j-1]
dirs = [(-1,0),(1,0),(0,-1),(0,1)]
def dfs(x,y):
    g[x][y] = 3
    for dx, dy in dirs:
        nx = x+dx
        ny = y+dy
        if 0<=nx<=n+1 and 0<=ny<=n+1 and g[nx][ny]==0:
            dfs(nx, ny)
dfs(0,0)
for i in range(1, n+1):
    print(' '.join(
        '2' if g[i][j] == 0 else '0' if g[i][j] == 3 else str(g[i][j])
        for j in range(1, n+1)
    ))