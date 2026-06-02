#dfs
rows, cols = 4, 4
dirs = [(-1,0), (1,0), (0,-1), (0,1)]
ans = 0
def dfs(x, y, step, vis):
    global ans
    # 走完16步，找到一种方案
    if step == 16:
        ans += 1
        return
    # 遍历四个方向
    for dx, dy in dirs:
        nx = x + dx
        ny = y + dy
        # 边界合法 + 未访问
        if 0 <= nx < rows and 0 <= ny < cols and not vis[nx][ny]:
            vis[nx][ny] = True
            dfs(nx, ny, step+1, vis)
            vis[nx][ny] = False
# 枚举每一个格子作为起点(数字1的位置)
for i in range(rows):
    for j in range(cols):
        # 初始化访问标记数组
        visit = [[False]*4 for _ in range(4)]
        visit[i][j] = True
        dfs(i, j, 1, visit)
print(ans)