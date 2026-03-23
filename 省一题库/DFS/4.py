n,k = map(int,input().split())

def dfs(s,used):
    if len(s.split()) == k:
        print(s)
        return
    for i in range(1,n+1):
        if i not in used:
            dfs(f"{s} {i}".strip(),used | {i})
dfs('',set())