n,p = map(int,input().split())
a = []
b = []
sum_a = 0
for _ in range(n):
    ai, bi = map(int, input().split())
    a.append(ai)
    b.append(bi)
    sum_a += ai
#所有设备的总消耗率 ≤ 充电宝的总充能率 时，才能无限运行。
if sum_a <= p:
    print(-1)
    exit()
l = 0.0
r = 1e14
for _ in range(100):
    # 判断能否通过充能让所有设备撑过 mid 秒
    mid = (l + r) / 2
    sum_t = 0.0 # 总需要充入的能量
    for i in range(n):
        # t秒内该设备需要的总能量 - 初始能量 = 缺口
        need = a[i] * mid - b[i]
        if need > 0:
            sum_t += need / p
    # 验证：所需充电时间 <= 总运行时间，说明mid可行
    if sum_t <= mid:
        l = mid
    else:
        r = mid
print(f"{l:.10f}")