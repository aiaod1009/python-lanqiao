n,m = map(int,input().split())
path = []
def dfs(start):
    # 终止条件：路径长度等于m，输出结果
    if len(path) == m:
        print(' '.join(map(str, path)))
        return

    # 核心优化：下一层从 start 开始，且最多选到 n - (m - len(path)) + 1
    # 这里直接写 range(1, n+1) 也能过，但加上剪枝效率更高
    for i in range(start, n + 1):
        path.append(i)  # 选第i个数
        dfs(i + 1)  # 下一个数从i+1开始，保证不重复、不逆序
        path.pop()  # 回溯

dfs(1)  # 从1开始选