# n,k = map(int,input().split())
#
# def dfs(s,used):
#     if len(s.split()) == k:
#         print(s)
#         return
#     for i in range(1,n+1):
#         if i not in used:
#             dfs(f"{s} {i}".strip(),used | {i})
# dfs('',set())

n, k = map(int, input().split())
res = [0] * k      # 结果数组，长度是 k（选k个人）
used = [False] * (n+1) # 标记是否用过（1~n）
def dfs(pos):
    if pos == k:
        print(' '.join(map(str,res)))
        return
    for i in range(1,n+1):
        if not used[i]:
            used[i] = True
            res[pos] = i
            dfs(pos+1)
            used[i] = False
dfs(0)
