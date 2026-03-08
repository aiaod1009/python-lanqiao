import os
import sys

# 请在此输入您的代码
n = 2021041820210418
a = 20210418
b = 100000001


def fenjie(num):
    f = {}
    while num % 2 == 0:
        f[2] = f.get(2, 0) + 1
        num //= 2

    i = 3
    while i * i <= num:
        while num % i == 0:
            f[i] = f.get(i, 0) + 1
            num //= i

        i += 2

    if num > 1:
        f[num] = 1
    return f


f_a = fenjie(a)
f_b = fenjie(b)

total = f_a.copy()
for p, e in f_b.items():
    total[p] = total.get(p, 0) + e

ans = 1
for e in total.values():
    ans *= (e + 1) * (e + 2) // 2

print(ans)

