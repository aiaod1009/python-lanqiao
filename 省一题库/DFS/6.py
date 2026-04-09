n = int(input())
plans = []
arr = [0] * 10

def dfs(step, s):
    # step：当前正在处理第step种配料（0~9，共10种）
    # s：当前已经累加的总质量
    if s > n:# 剪枝：当前总质量已经超过n，后续只会更大，直接返回
        return
    if step == 10:
        if s == n:
            plans.append(arr.copy())
        return
    for g in [1, 2, 3]:
        arr[step] = g
        dfs(step + 1, s + g)
dfs(0, 0)

print(len(plans))
for plan in plans:
    print(' '.join(map(str, plan)))