import sys
sys.setrecursionlimit(1 << 25)

N, M = map(int, sys.stdin.readline().split())
graph = [[] for _ in range(N + 1)]
for _ in range(M):
    a, b = map(int, sys.stdin.readline().split())
    graph[a].append(b)
    graph[b].append(a)

visited = [False] * (N + 1)
cnt = 0

def dfs(u):
    visited[u] = True
    for v in graph[u]:
        if not visited[v]:
            dfs(v)

for i in range(1, N + 1):
    if not visited[i]:
        cnt += 1
        dfs(i)

min_line = cnt - 1
if cnt == 1:
    max_degree = 0
elif cnt == 2:
    max_degree = 1
else:
    max_degree = 2

print(min_line, max_degree)