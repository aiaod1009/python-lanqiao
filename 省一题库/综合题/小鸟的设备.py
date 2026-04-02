n,p = map(int,input().split())
a = []
b = []
sum_a = 0
for _ in range(n):
    ai, bi = map(int, input().split())
    a.append(ai)
    b.append(bi)
    sum_a += ai
if sum_a <= p:
    print(-1)
    exit()
l = 0.0
r = 1e14
for _ in range(100):
    mid = (l + r) / 2
    sum_t = 0.0
    for i in range(n):
        need = a[i] * mid - b[i]
        if need > 0:
            sum_t += need / p
    if sum_t <= mid:
        l = mid
    else:
        r = mid
print("{0:.10f}".format(l))