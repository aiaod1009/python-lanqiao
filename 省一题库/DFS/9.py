n = int(input().strip())
def dfs(path,last):
    s = sum(path)
    if s == n:
        print('+'.join(map(str,path)))
        return
    re = n - s
    for i in range(last,re + 1):
        if i < n:
            dfs(path + [i],i)
dfs([],1)


