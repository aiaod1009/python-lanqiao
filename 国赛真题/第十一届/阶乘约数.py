primes = []
for i in range(2, 101):
    f = True
    for j in range(2, int(i ** 0.5) + 1):
        if i % j == 0:
            f = False
            break
    if f:
        primes.append(i)
#计算每个质数在 100! 中的指数，并直接累乘计算约数个数
tot = 1
for p in primes:
    e = 0
    temp = 100
    # 勒让德定理：不断除以 p 并累加商
    while temp > 0:
        e += temp // p
        temp //= p
    # 约数个数定理：每个质数的(指数 + 1)相乘
    tot *= (e + 1)
print(tot)