a = [0,5,5,10,10,15,15,20,20,25,25]
b = [0] * 151
def dfs(k, s):
    if k > 10:
        b[s] = 1
        return
    dfs(k+1, s)  # 不选这个数
    dfs(k+1, s+a[k])  # 选这个数

dfs(0, 0)
print(sum(b))