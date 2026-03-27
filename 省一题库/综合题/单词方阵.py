import sys
input = lambda:sys.stdin.readline().strip()
n = int(input())
g = [input() for _ in range(n)]
t = "yizhong"
d = [(-1,-1),(-1,0),(-1,1),(0,-1),(0,1),(1,-1),(1,0),(1,1)]
m = [[0]*n for _ in range(n)]   # 标记数组
for i in range(n):
    for j in range(n):
        if g[i][j] != 'y':continue
        for dx,dy in d:
            #先判断能不能走 7 步
            if 0 <= i+6*dx < n and 0 <= j+6*dy < n:
                ok = 1
                # 八个方向各走七步尝试能不能拼出来
                for k in range(7):
                    # t[k]：目标单词 yizhong 的第 k 个字母
                    if g[i+k*dx][j+k*dy] != t[k]:
                        ok = 0
                        break
                if ok:
                    for k in range(7):
                        m[i+k*dx][j+k*dy] = 1
for i in range(n):
    print(''.join(g[i][j] if m[i][j] else '*' for j in range(n)))