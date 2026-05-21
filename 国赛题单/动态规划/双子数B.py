import math
# 第一步：筛质数（埃氏筛法）
max_k = 4830459  # sqrt(23333333333333)
is_prime = [True] * (max_k + 1)
is_prime[0] = is_prime[1] = False
#is_prime 是一个布尔数组，用来标记数字是不是质数。一开始先把 0 和 1 标记为非质数。
for i in range(2, int(math.isqrt(max_k)) + 1):
    if is_prime[i]:  #如果它是质数（is_prime[i] 为 True）
        #就把它的所有倍数（从 i*i 开始，步长为 i）标记为非质数。
        for j in range(i*i, max_k+1, i):
            is_prime[j] = False
#把所有标记为 True 的数（也就是质数）存进 primes 列表里。
primes = [i for i, val in enumerate(is_prime) if val]
# 第二步：数符合条件的双子数
ans = 0
L = 2333
R = 23333333333333
n = len(primes)
for i in range(n):
    p = primes[i]
    if p**4 > R:
        break
    for j in range(i+1, n):
        q = primes[j]
        num = (p*q)**2
        if num > R:
            break
        if num >= L:
            ans += 1
print(ans)