n = int(input())
plans = []
arr = [0] * 10

def dfs(step, s):
    if s > n:
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