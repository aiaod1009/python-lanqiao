# bfs题(先进先出)
from collections import deque
n, a, b = map(int, input().split())
k = [0]+list(map(int, input().split()))
# 记录到每层的最少按键次数，-1 表示没访问过
dist = [-1] * (n + 1)
q = deque()
# 起点：a 楼，次数 0
dist[a] = 0
q.append(a)
while q:   # 只要队列不为空，就继续遍历
    cur = q.popleft()   # 从队列左边取出「当前要处理的楼层」
    if cur == b:  # 如果已经到目标楼，直接结束
        break
    # 当前层的 K 值
    ki = k[cur]  # 因为 k 是 0 开头，cur 是 1 开头
    for d in (-1, 1):
        next_floor = cur + d * ki  # 计算按上/下后要去的楼层
        # 判断：新楼层在 [1,n] 范围内，且没被访问过
        if 1 <= next_floor <= n and dist[next_floor] == -1:
            dist[next_floor] = dist[cur] + 1  # 步数 = 当前步数 +1
            q.append(next_floor)            # 把新楼层放进队列，之后处理
print(dist[b])


# 不用队列，用列表模拟先进先出
n, a, b = map(int, input().split())
k = [0] + list(map(int, input().split()))
dist = [-1] * (n + 1)
dist[a] = 0  # 起点步数为 0
# 用列表模拟队列：current 是当前层要处理的楼层
current = [a]
while current:
    next_level = []  # 存下一层要处理的楼层
    for cur in current:
        if cur == b:
            break  # 找到目标，提前终止
        ki = k[cur]
        # 尝试下、上两个方向
        for d in (-1, 1):
            nxt = cur + d * ki
            if 1 <= nxt <= n and dist[nxt] == -1:
                dist[nxt] = dist[cur] + 1
                next_level.append(nxt)
    current = next_level  # 进入下一层
print(dist[b])