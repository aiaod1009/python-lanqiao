n = int(input().strip())
res = ['']*3
def dfs(pos):
    if pos == n:
        print(''.join(map(str,res)))
        return
