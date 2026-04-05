#暴搜
n,s = map(int,input().split())
a = []
vis = [0] * 13
ok = False
def calc():
    temp = a.copy()
    while len(temp) > 1:
        # new = []
        # for i in range(len(temp)-1):
        #     new.append(temp[i] + temp[i+1])
        # temp = new
        temp = [temp[i] + temp[i + 1] for i in range(len(temp) - 1)]
    return temp[0]
def dfs(dep):
    global ok
    if ok:
        return
    if dep == n:
        if calc() == s:
            print(' '.join(map(str,a)))
            ok = True
        return
    for i in range(1,n+1):
        if not vis[i]:
            vis[i] = 1   # 标记数字 i 已经被使用
            a.append(i)
            dfs(dep+1)
            a.pop()
            vis[i] = 0
            if ok:
                return
dfs(0)