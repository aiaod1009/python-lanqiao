n = int(input().strip())
res = ['']*n
def dfs(pos):
    if pos == n:
        print(''.join(res))
        return
    res[pos] = 'N'
    dfs(pos+1)
    res[pos] = 'Y'
    dfs(pos+1)

dfs(0)