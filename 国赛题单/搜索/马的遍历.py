from collections import deque
n,m,x,y = map(int,input().split())
dist = [[-1] * (m+1) for _ in range(n+1)]
dx = [2, 2, -2, -2, 1, 1, -1, -1]
dy = [1, -1, 1, -1, 2, -2, 2, -2]
q = deque()
dist[x][y] = 0
q.append((x,y))
while q:
    cx,cy = q.popleft()
    for i in range(8):
        nx = cx + dx[i]
        ny = cy + dy[i]
        if 1 <= nx <= n and 1 <= ny <= m and dist[nx][ny] == -1:
            dist[nx][ny] = dist[cx][cy] + 1
            q.append((nx,ny))
for i in range(1,n+1):
    print(' '.join(map(str,dist[i][1:m+1])))