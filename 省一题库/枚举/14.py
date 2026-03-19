import sys
input = lambda :sys.stdin.readline()
MI = lambda: map(int, input().split())

def solve():
    b = sorted(MI())
    cnta,cntb = MI()
    va,vb = MI()
    if va>vb:  # 保证：A 的体积 ≤ B 的体积（方便后面贪心）
        va,vb = vb,va     # 交换 A 和 B 的体积
        cnta,cntb = cntb,cnta  # 同时交换数量，不然就搞混了
    res = 0        # 记录最多能装多少个积木
    # i：背包0（最小的背包）放的 A 数量
    for i in range(min(cnta,b[0]//va)+1):
        cnt_b1 = min(cntb, (b[0]-i*va)//vb)  # 背包0最多能放的 B 数量
        # j：背包1（中间的背包）放的 A 数量（不能超过剩余 A 数量）
        for j in range(min(cnta-i, b[1]//va)+1):
            cnt_b2 = min(cntb-cnt_b1, (b[1]-j*va)//vb)  # 背包1最多能放的 B 数量
            # 背包3（最大的背包）：优先放体积小的 A，一定最优
            k = min(cnta-i-j, b[2]//va)  # 最多能放的 A 数量
            cnt_b3 = min(cntb-cnt_b1-cnt_b2, (b[2]-k*va)//vb) # 剩余空间放 B

            # 更新最大总数量
            res = max(res, i+j+k+cnt_b1+cnt_b2+cnt_b3)
    print(res)

if __name__=='__main__':
    n = int(input().strip())
    for _ in range(n):
        solve()

# ✅ 前两个背包：枚举（试所有可能的 A 数量）
# ✅ 第三个背包：贪心（直接算最优的 A 数量，不用试）