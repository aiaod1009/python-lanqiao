n, m = map(int, input().split())
g = [input().strip() for _ in range(n)]
max_val = 0
def dfs(row):
    global max_val
    if row == n:
        # 计算当前价值
        res = 0
        for i in range(n):
            for j in range(m):
                cnt = 0
                if i > 0 and g[i - 1][j] == g[i][j]: cnt += 1
                if i < n - 1 and g[i + 1][j] == g[i][j]: cnt += 1
                if j > 0 and g[i][j - 1] == g[i][j]: cnt += 1
                if j < m - 1 and g[i][j + 1] == g[i][j]: cnt += 1
                res += cnt * cnt
        if res > max_val:
            max_val = res
        return
    # 不翻转当前行
    dfs(row + 1)
    # 翻转当前行
    old = g[row]
    g[row] = ''.join('1' if c == '0' else '0' for c in g[row])
    dfs(row + 1)
    g[row] = old  # 回溯
dfs(0)
print(max_val)