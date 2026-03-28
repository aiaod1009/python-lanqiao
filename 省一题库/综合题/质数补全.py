N = int(input().strip())
res = []
def dfs(idx,s,tot,last):
    if idx == N + 1:
        if tot == 0:
            res.append(s)
    dfs(idx+1,s+" "+str(idx),tot-last+last*10+(idx if last > 0 else - idx))

