n,d = map(int,input().split())
v = list(map(int,input().split()))
a = list(map(int,input().split()))
b = 0

INF = float('inf')
mi = INF  # 从起点到当前站点，所有加油站里最便宜的油价
ans = 0
s = 0
for i in range(n-1):  # 对应多少段路
    price = a[i]
    dist = v[i]
    s += dist  # 欠的公里数
    mi = min(mi,price)
    if s > 0:
        need = (s+d-1) // d  # 向上取整写法
        ans += need * mi
        s -= need * d
print(ans)