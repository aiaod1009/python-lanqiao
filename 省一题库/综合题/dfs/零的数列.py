def dfs(idx, expr, total, last):
    if idx == N + 1:
        if total == 0:
            res.append(expr)
        return
    # 空格（拼接数字）
    dfs(idx + 1, expr + " " + str(idx),
        total - last + last * 10 + (idx if last > 0 else -idx),
        last * 10 + (idx if last > 0 else -idx))
    # + 号
    dfs(idx + 1, expr + "+" + str(idx), total + idx, idx)
    # - 号
    dfs(idx + 1, expr + "-" + str(idx), total - idx, -idx)

N = int(input())
res = []
dfs(2, "1", 1, 1)
for s in res:
    print(s)