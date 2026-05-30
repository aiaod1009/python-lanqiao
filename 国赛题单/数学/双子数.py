import math
L, R = 49, 4830458
is_prime = [True] * (R + 1)
primes = []
for i in range(2, R + 1):
    if is_prime[i]:
        primes.append(i)
        for j in range(i * i, R + 1, i):
            is_prime[j] = False
ans = 0
for i in range(len(primes)):
    p = primes[i]
    if p * p > R:
        break
    for j in range(i + 1, len(primes)):
        q = primes[j]
        product = p * q
        if product > R:  # 爆上限了，后面的 q 更大，直接切断内层
            break
        if product >= L:  # 落在区间内，合格
            ans += 1

print(ans)