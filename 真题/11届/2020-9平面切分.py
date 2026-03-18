n = int(input())
lines = set()
for _ in range(n):
    a,b = map(int,input().split())
    lines.add((a,b))

l = list(lines)
m = len(l)
points = set()

for i in range(m):
    a1,b1 = l[i]
    for j in range(i + 1,m):
        a2,b2 = l[j]
        if a1 == a2:
            continue
        x = round((b2 - b1) / (a1 - a2))
        y = round(a1 * x + b1)
        points.add((x,y))

res = 1 + m + len(points)
print(res)
