# N = int(input())
# l = [i**2 for i in range(int(N**0.5))]
# ans = []
# while N >= 0:
#     for x in range(len(l)):
#         for y in range(len(l)):
#             for z in range(len(l)):
#                 e = (N - (l[x] + l[y] + l[z]))**0.5
#                 if l[x] + l[y] + l[z] + e**2 == N:
#                     ans.append(x)
#                     ans.append(y)
#                     ans.append(z)
#                     ans.append(e)
# print(' '.join(str(i) for i in ans))

import math
N = int(input())
max_a = int(math.isqrt(N))
for a in range(max_a + 1):
    rem1 = N - a * a
    max_b = int(math.isqrt(rem1))
    for b in range(a, max_b + 1):  # 保证 a <= b
        rem2 = rem1 - b * b
        max_c = int(math.isqrt(rem2))
        for c in range(b, max_c + 1):  # 保证 b <= c
            d2 = rem2 - c * c
            d = int(math.isqrt(d2))
            if d * d == d2 and d >= c:  # 保证 c <= d
                print(a, b, c, d)
                exit()  # 找到第一个解就退出，保证字典序最小

