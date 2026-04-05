ans = 0
a = [0] * 26  # a[1]~a[25] 存棋盘，1=白棋，0=黑棋
r = 0  # 白棋数量
t = 0  # 黑棋数量

def pd():
    global ans
    # 检查 5 行
    if (a[1]+a[2]+a[3]+a[4]+a[5]) % 5 == 0:return
    if (a[6]+a[7]+a[8]+a[9]+a[10]) % 5 == 0:return
    if (a[11]+a[12]+a[13]+a[14]+a[15]) % 5 == 0:return
    if (a[16]+a[17]+a[18]+a[19]+a[20]) % 5 == 0:return
    if (a[21]+a[22]+a[23]+a[24]+a[25]) % 5 == 0:return
    # 检查 5 列
    if (a[1]+a[6]+a[11]+a[16]+a[21]) % 5 == 0:return
    if (a[2]+a[7]+a[12]+a[17]+a[22]) % 5 == 0:return
    if (a[3]+a[8]+a[13]+a[18]+a[23]) % 5 == 0:return
    if (a[4]+a[9]+a[14]+a[19]+a[24]) % 5 == 0:return
    if (a[5]+a[10]+a[15]+a[20]+a[25]) % 5 == 0:return
    # 检查 2 条斜线
    if (a[1]+a[7]+a[13]+a[19]+a[25]) % 5 == 0:return
    if (a[5]+a[9]+a[13]+a[17]+a[21]) % 5 == 0:return
    # 所有线都没五子连珠 → 平局，计数+1
    ans += 1

def dfs(k):
    global r, t
    if k == 26:  # 下满 25 格（k 从 1 到 25）
        pd()
        return
    # 尝试放白棋（最多 13 颗）
    if r <= 12:
        a[k] = 1
        r += 1
        dfs(k + 1)
        r -= 1
    # 尝试放黑棋（最多 12 颗）
    if t <= 11:
        a[k] = 0
        t += 1
        dfs(k + 1)
        t -= 1
dfs(1)
print(ans)