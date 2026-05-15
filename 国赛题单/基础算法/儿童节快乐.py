import math
k = 10120300500
prod = 2 * k
total = 0
for d in range(1, math.isqrt(prod) + 1):
    if prod % d == 0:
        e = prod // d
        if (d + e) % 2 == 0:  #必须是偶数
            a = (d + e) // 2
            n = a * a - k
            total += n
print(total)