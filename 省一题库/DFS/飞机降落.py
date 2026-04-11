import sys
input = lambda:sys.stdin.readline().strip()
def dfs(vis,now):
    if all(vis):
        return True
    for i in range(n):
        if not vis[i]:
            t,d,l = a[i]
            if now > t+d:  #第 i 架飞机最晚必须降落的时间
                continue
            s = max(now,t)  # 真正开始降落的时间 = 等跑道 或 等飞机，取晚的那个
            if s > t + d:   # 开始时间都晚于最晚时间 → 不行
                continue
            vis[i] = 1
            if dfs(vis,s + l):  # 这架飞机降落结束的时间
                return True
            vis[i] = 0
    return False

for _ in range(int(input())):
    n = int(input())
    a = [list(map(int,input().split())) for _ in range(n)]
    print("YES" if dfs([0]*n,0) else "NO")
