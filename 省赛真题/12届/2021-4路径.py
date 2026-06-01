import heapq
import math
def lcm(a, b):
    return a * b // math.gcd(a, b)
n = 2021
INF = float('inf')
dist = [INF] * (n + 1)
dist[1] = 0  # 起点是1，距离为0
# 优先队列，存储 (距离, 结点)
heap = []
heapq.heappush(heap, (0, 1))
while heap:
    current_dist, u = heapq.heappop(heap)

    # 如果当前距离已经大于记录的最短距离，跳过
    if current_dist > dist[u]:
        continue
    # 遍历所有可能的邻居 v = u + k, k从1到21
    for k in range(1, 22):
        v = u + k
        if v <= n:
            weight = lcm(u, v)
            if dist[v] > dist[u] + weight:
                dist[v] = dist[u] + weight
                heapq.heappush(heap, (dist[v], v))
    # 遍历所有可能的邻居 v = u - k, k从1到21
    for k in range(1, 22):
        v = u - k
        if v >= 1:
            weight = lcm(u, v)
            if dist[v] > dist[u] + weight:
                dist[v] = dist[u] + weight
                heapq.heappush(heap, (dist[v], v))
print(dist[2021])
