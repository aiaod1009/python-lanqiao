n = int(input())
res = []
col = [False] * (n + 1)       # 列 1~n
diag1 = [False] * (2 * n)     # 主对角线：row - col + (n - 1)偏移量防止负数
diag2 = [False] * (2 * n)     # 副对角线：row + col
def dfs(row, path):  # row：正在处理第几行（从 0 开始）path：是一个列表，存每一行的列号
    if row == n:
        res.append(path.copy())
        return
    for c in range(1, n+1):
        #来判断斜着会不会撞
        d1 = row - c + n - 1   # 主对角线：row - col + n - 1
        d2 = row + c           # 副对角线：row + col
        #这行代码是能否放皇后的准入门槛，三个条件必须同时满足
        if not col[c] and not diag1[d1] and not diag2[d2]:
            col[c] = True
            diag1[d1] = True
            diag2[d2] = True
            path.append(c)
            dfs(row + 1, path)
            #回溯（撤销标记）
            path.pop()
            diag2[d2] = False
            diag1[d1] = False
            col[c] = False

dfs(0, [])
for i in range(min(3, len(res))):
    print(' '.join(map(str, res[i])))
print(len(res))