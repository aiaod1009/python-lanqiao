cost = [6, 2, 5, 5, 4, 5, 6, 3, 7, 6]

def d(x):
    if x == 0:
        return cost[0]
    s = 0
    while x > 0:
        s += cost[x % 10]
        x = x // 10
    return s

n = int(input())
ans = 0
for a in range(1000):
    for b in range(1000):
        c = a + b
        total = d(a) + d(b) + d(c) + 4  # +和=用4根
        if total == n:
            ans += 1

print(ans)