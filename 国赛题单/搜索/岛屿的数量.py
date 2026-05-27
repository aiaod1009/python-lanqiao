from collections import deque
n = int(input().strip())
grid = [list(map(int,input().split())) for _ in range(n)]
cnt = 0
dirs = [(-1,0),(1,0),(0,-1),(0,1)]
for i in range(n):
    for j in range(n):
        if grid[i][j] == 1:
            cnt += 1
            q = deque([(i,j)])
            grid[i][j] = 0
            while q:
                x,y = q.popleft()
                for dx,dy in dirs:
                    nx,ny = x + dx,y + dy
                    if 0 <= nx <= n and 0 <= ny <= n and grid[nx][ny] == 1:
                        grid[nx][ny] = 0
                        q.append((nx,ny))
print(cnt)