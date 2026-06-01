# def comb(r, k):
#     if k < 0 or k > r:
#         return 0
#     if k == 0 or k == r:
#         return 1
#     k = min(k, r - k)  # 利用对称性减少计算
#     res = 1
#     for i in range(1, k + 1):
#         res = res * (r - k + i) // i
#     return res
#
#
# n = int(input())
#
# if n == 1:
#     print(1)
# else:
#     minp = float('inf')
#     k = 1
#     while True:
#         if comb(k + 1, k) > n:
#             break
#         l = k
#         r = n
#         while l <= r:
#             mid = (l + r) // 2
#             c = comb(mid, k)
#
#             if c == n:
#                 row = mid + 1
#                 col = k + 1
#                 p = (row - 1) * row // 2 + col
#                 if p < minp:
#                     minp = p
#                 break
#             elif c < n:
#                 l = mid + 1
#             else:
#                 r = mid - 1
#         k += 1
#     print(minp)

import os
import sys

# 请在此输入您的代码
a = int(input())
l = [1, 1, 1, 1, 2, 1, 1, 3, 3, 1]
if a in l:
    print(l.index(a)+1)
else:
    temp = False
    for m in range(4, 45000):
        last = m
        if a == last:
            temp = True
            print(m * (1 + m) // 2 + 2)
            break
        for n in range(2, m//2+1):
            last = last*(m+1-n)//n
            if a == last:
                print(m*(1+m)//2+n+1)
                temp = True
                break
            if last > 1000000000:
                break
        if temp:
            break
    if not temp:
        print(a*(1+a)//2+2)

# 直接打表拿20%