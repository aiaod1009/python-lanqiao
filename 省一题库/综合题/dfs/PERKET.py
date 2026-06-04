#python3的ac代码
import sys
input = lambda:sys.stdin.readline().strip()
n = int(input())
f = [tuple(map(int, input().split())) for _ in range(n)]
def dfs(idx, s, b):
    if idx == n: #出口
        if s == 1 and b == 0:
            return float('inf')  # 空方案返回无穷大，不影响最小值
        return abs(s - b)
    # 不选当前 + 选当前，取最小值
    return min(dfs(idx + 1, s, b), dfs(idx + 1, s * f[idx][0], b + f[idx][1]))
print(dfs(0, 1, 0))

# pypy的ac代码
n = int(input())
foods = [tuple(map(int, input().split())) for _ in range(n)]
min_diff = float('inf')
def dfs(idx, s, b, cnt):
    global min_diff
    if idx == n:
        if cnt > 0:  # 必须至少选一种
            min_diff = min(min_diff, abs(s - b))
        return
    dfs(idx + 1, s, b, cnt)
    dfs(idx + 1, s * foods[idx][0], b + foods[idx][1], cnt + 1)
dfs(0, 1, 0, 0)
print(min_diff)