import sys

# n = int(input())
# a = list(map(int,sys.stdin().readline().split()))
# a.sort()
# pre = [0] * (n + 1)
# ans = 0
# for i in range(n):
#     pre[i+1] = pre[i] + a[i]
#     ans += a[i] * i - pre[i]
# print(ans)


n = int(input())
a = [0] + list(map(int, input().split()))
ans = 0
for j in range(20):
    c = 0
    d = 0
    u = 0
    v = 0
    for i in range(1, n + 1):
        q = (a[i] >> j) & 1
        if q == 1:
            ans += (i*c - u) * (1 << j)
            d += 1
            v += i
        else:
            ans += (i*d - v) * (1 << j)
            c += 1
            u += i
print(ans)