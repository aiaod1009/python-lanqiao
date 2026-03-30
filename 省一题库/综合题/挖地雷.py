n = int(input())
v = [0]+list(map(int,input().split()))
g = [[] for _ in range(n+1)]
for i in range(1,n):
   g[i] = [i+j+1 for j,x in enumerate(map(int,input().split())) if x]
# m：用来记录挖到的最大地雷总数,p：用来记录对应那条最优路径
m,p = 0,[]
# u：当前所在的地窖编号。
# s：走到当前地窖时，累计的地雷总数。
# path：目前走过的路径列表（例如 [1, 3]）
def dfs(u,s,path):
    global m,p
    if s > m:
        m,p = s,path
    for w in g[u]:
        dfs(w,s+v[w],path+[w])
for u in range(1,n+1):
    dfs(u,v[u],[u])
print(' '.join(map(str,p)))
print(m)