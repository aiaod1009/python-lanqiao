n = int(input())
f = [tuple(map(int, input().split())) for _ in range(n)]

def dfs(idx, s, b):
    if idx == n:
        if s == 1 and b == 0:
            return float('inf')  # 空方案返回无穷大，不影响最小值
        return abs(s - b)
    # 不选当前 + 选当前，取最小值
    return min(dfs(idx + 1, s, b), dfs(idx + 1, s * f[idx][0], b + f[idx][1]))

print(dfs(0, 1, 0))