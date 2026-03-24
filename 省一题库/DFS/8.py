ans = 0
def dfs(x, y, step):
    global ans
    # 糖果不能为负
    if x < 0 or y < 0:
        return
    # 7个人分完了
    if step == 7:
        # 必须两种糖都分完
        if x == 0 and y == 0:
            ans += 1
        return

    # 枚举第i个小朋友拿第一种糖的数量
    for i in range(x + 1):
        # 枚举第i个小朋友拿第二种糖的数量
        for j in range(y + 1):
            # 核心约束：每人总数在 2~5 之间
            if 2 <= i + j <= 5:
                dfs(x - i, y - j, step + 1)


# 初始状态：9个、16个、0个人
dfs(9, 16, 0)
print(ans)