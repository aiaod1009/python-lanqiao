n = int(input().strip())
a = sorted(list(map(int,input().split())))
l = 0
r = n // 2
res = 0
while l < n // 2 and r <n:
    if a[r] >= 2 * a[l]:
        res += 1
        l += 1
        r += 1
    else:
        r += 1
print(res)